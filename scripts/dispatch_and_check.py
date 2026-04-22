#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_TEMPLATE = Path('a2a_dispatch_template.md')


def run_cmd(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True)


def send_message(session_key: str, message: str) -> dict:
    proc = run_cmd([
        'openclaw', 'gateway', 'call', 'sessions.send', '--json', '--params',
        json.dumps({'key': session_key, 'message': message}, ensure_ascii=False)
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'sessions.send failed')
    return json.loads(proc.stdout)


def check_ack(session_key: str, task_id: str) -> dict:
    proc = run_cmd(['python3', 'ack_check.py', '--session-key', session_key, '--task-id', task_id])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'ack_check.py failed')
    return json.loads(proc.stdout)


def build_message(project_id: str, task_id: str, pm_owner: str, file_path: str, request_summary: str) -> str:
    return (
        f'project_id={project_id}\n'
        f'task_id={task_id}\n'
        f'pm_owner={pm_owner}\n'
        f'file_path={file_path}\n'
        f'request_summary={request_summary}\n'
        'expected_reply=ACK|BLOCKED\n\n'
        '请先读取以下主线文件：\n'
        '- 00-brief/brief.md\n'
        '- 01-status/status.json\n'
        '- 01-status/next-step.md\n'
        '- 如有必要，再读取 02-decisions/decision-log.md\n\n'
        '请基于项目文件继续执行，不要脱离共享目录主线。\n'
        '如可执行，请仅回复 ACK。\n'
        '如无法执行，请仅回复 BLOCKED，并说明 exact blocker。'
    )


def main() -> None:
    parser = argparse.ArgumentParser(description='Send A2A dispatch and optionally check ACK.')
    parser.add_argument('--session-key', required=True)
    parser.add_argument('--project-id', required=True)
    parser.add_argument('--task-id', required=True)
    parser.add_argument('--pm-owner', required=True)
    parser.add_argument('--file-path', required=True)
    parser.add_argument('--request-summary', required=True)
    parser.add_argument('--check-ack', action='store_true')
    args = parser.parse_args()

    message = build_message(
        project_id=args.project_id,
        task_id=args.task_id,
        pm_owner=args.pm_owner,
        file_path=args.file_path,
        request_summary=args.request_summary,
    )

    send_result = send_message(args.session_key, message)
    result = {
        'dispatch': {
            'session_key': args.session_key,
            'project_id': args.project_id,
            'task_id': args.task_id,
            'pm_owner': args.pm_owner,
            'file_path': args.file_path,
            'send_result': send_result,
        }
    }

    if args.check_ack:
        result['ack_check'] = check_ack(args.session_key, args.task_id)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
