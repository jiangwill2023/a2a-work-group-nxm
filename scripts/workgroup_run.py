#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

SETTINGS_PATH = Path('config/settings.json')


def load_settings() -> dict:
    if SETTINGS_PATH.exists():
        return json.loads(SETTINGS_PATH.read_text(encoding='utf-8'))
    return {'shared_root': 'YOUR_SHARED_ROOT'}


SHARED_ROOT = Path(load_settings().get('shared_root', 'YOUR_SHARED_ROOT'))


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True)


def create_project(project_name: str, shortname: str, requester: str, pm_owner: str, assistants: list[str] | None = None, finance_support: list[str] | None = None) -> dict:
    assistants = assistants or []
    finance_support = finance_support or []
    proc = run([
        'python3', 'project_create.py',
        '--project-name', project_name,
        '--shortname', shortname,
        '--requester', requester,
        '--pm-owner', pm_owner,
        '--assistants', ','.join(assistants),
        '--finance-support', ','.join(finance_support),
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'project_create.py failed')
    return json.loads(proc.stdout)


def dispatch(session_key: str, project_id: str, task_id: str, pm_owner: str, file_path: str, request_summary: str) -> dict:
    proc = run([
        'python3', 'dispatch_and_check.py',
        '--session-key', session_key,
        '--project-id', project_id,
        '--task-id', task_id,
        '--pm-owner', pm_owner,
        '--file-path', file_path,
        '--request-summary', request_summary,
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'dispatch_and_check.py failed')
    return json.loads(proc.stdout)


def ack_check(session_key: str, task_id: str) -> dict:
    proc = run([
        'python3', 'ack_check.py',
        '--session-key', session_key,
        '--task-id', task_id,
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'ack_check.py failed')
    return json.loads(proc.stdout)


def wait_for_ack(session_key: str, task_id: str, wait_seconds: int, poll_interval: int) -> dict:
    deadline = time.time() + wait_seconds
    last = None
    while time.time() <= deadline:
        last = ack_check(session_key, task_id)
        if last.get('status') in ('ACKED', 'BLOCKED'):
            return last
        time.sleep(poll_interval)
    return last or {
        'task_id': task_id,
        'status': 'IN_PROGRESS',
        'session_key': session_key,
        'reply_seq': None,
        'evidence': ''
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Run end-to-end workgroup flow: create project -> dispatch -> wait for ACK.')
    parser.add_argument('--project-name', required=True)
    parser.add_argument('--shortname', required=True)
    parser.add_argument('--requester', required=True)
    parser.add_argument('--pm-owner', required=True)
    parser.add_argument('--session-key', required=True)
    parser.add_argument('--task-id', required=True)
    parser.add_argument('--request-summary', required=True)
    parser.add_argument('--wait-seconds', type=int, default=30)
    parser.add_argument('--poll-interval', type=int, default=5)
    parser.add_argument('--assistants', default='')
    parser.add_argument('--finance-support', default='')
    args = parser.parse_args()

    assistants = [x for x in args.assistants.split(',') if x]
    finance_support = [x for x in args.finance_support.split(',') if x]
    created = create_project(args.project_name, args.shortname, args.requester, args.pm_owner, assistants, finance_support)
    project_id = created['project_id']
    file_path = f'{SHARED_ROOT}{project_id}/'

    dispatched = dispatch(
        session_key=args.session_key,
        project_id=project_id,
        task_id=args.task_id,
        pm_owner=args.pm_owner,
        file_path=file_path,
        request_summary=args.request_summary,
    )

    ack = wait_for_ack(
        session_key=args.session_key,
        task_id=args.task_id,
        wait_seconds=args.wait_seconds,
        poll_interval=args.poll_interval,
    )

    result = {
        'created': created,
        'dispatch': dispatched,
        'ack': ack,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
