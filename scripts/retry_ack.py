#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess
import time


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True)


def ack_check(session_key: str, task_id: str) -> dict:
    proc = run(['python3', 'ack_check.py', '--session-key', session_key, '--task-id', task_id])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'ack_check.py failed')
    return json.loads(proc.stdout)


def retry_ack(session_key: str, task_id: str, wait_seconds: int, poll_interval: int) -> dict:
    deadline = time.time() + wait_seconds
    attempts = []
    last = None
    while time.time() <= deadline:
        last = ack_check(session_key, task_id)
        attempts.append(last)
        if last.get('status') in ('ACKED', 'BLOCKED'):
            return {'final': last, 'attempts': attempts}
        time.sleep(poll_interval)
    return {'final': last or {'status': 'IN_PROGRESS'}, 'attempts': attempts}


def main() -> None:
    parser = argparse.ArgumentParser(description='Retry ACK check until ACKED/BLOCKED or timeout.')
    parser.add_argument('--session-key', required=True)
    parser.add_argument('--task-id', required=True)
    parser.add_argument('--wait-seconds', type=int, default=30)
    parser.add_argument('--poll-interval', type=int, default=5)
    args = parser.parse_args()
    print(json.dumps(retry_ack(args.session_key, args.task_id, args.wait_seconds, args.poll_interval), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
