#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True)


def route_pm_owner(task_type: str, need_finance_support: bool) -> dict:
    cmd = ['python3', 'route_pm_owner.py', '--task-type', task_type]
    if need_finance_support:
        cmd.append('--need-finance-support')
    proc = run(cmd)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'route_pm_owner.py failed')
    return json.loads(proc.stdout)


def workgroup_run(project_name: str, shortname: str, requester: str, task_type: str, session_key: str, task_id: str, request_summary: str, wait_seconds: int, poll_interval: int, need_finance_support: bool) -> dict:
    routed = route_pm_owner(task_type, need_finance_support)
    proc = run([
        'python3', 'workgroup_run.py',
        '--project-name', project_name,
        '--shortname', shortname,
        '--requester', requester,
        '--pm-owner', routed['pm_owner'],
        '--session-key', session_key,
        '--task-id', task_id,
        '--request-summary', request_summary,
        '--wait-seconds', str(wait_seconds),
        '--poll-interval', str(poll_interval),
        '--assistants', ','.join(routed.get('assistants', [])),
        '--finance-support', ','.join(routed.get('finance_support', [])),
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'workgroup_run.py failed')
    return {
        'routing': routed,
        'run': json.loads(proc.stdout),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Auto route pm_owner and run end-to-end workgroup flow.')
    parser.add_argument('--project-name', required=True)
    parser.add_argument('--shortname', required=True)
    parser.add_argument('--requester', required=True)
    parser.add_argument('--task-type', required=True)
    parser.add_argument('--session-key', required=True)
    parser.add_argument('--task-id', required=True)
    parser.add_argument('--request-summary', required=True)
    parser.add_argument('--wait-seconds', type=int, default=30)
    parser.add_argument('--poll-interval', type=int, default=5)
    parser.add_argument('--need-finance-support', action='store_true')
    args = parser.parse_args()

    result = workgroup_run(
        project_name=args.project_name,
        shortname=args.shortname,
        requester=args.requester,
        task_type=args.task_type,
        session_key=args.session_key,
        task_id=args.task_id,
        request_summary=args.request_summary,
        wait_seconds=args.wait_seconds,
        poll_interval=args.poll_interval,
        need_finance_support=args.need_finance_support,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
