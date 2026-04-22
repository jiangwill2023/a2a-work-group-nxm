#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True)


def dispatch_one(session_key: str, project_id: str, task_id: str, pm_owner: str, file_path: str, request_summary: str) -> dict:
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
        return {'session_key': session_key, 'status': 'SEND_FAILED', 'error': proc.stderr.strip()}
    return json.loads(proc.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description='Dispatch same project task to multiple session targets.')
    parser.add_argument('--project-id', required=True)
    parser.add_argument('--task-id-prefix', required=True)
    parser.add_argument('--pm-owner', required=True)
    parser.add_argument('--file-path', required=True)
    parser.add_argument('--request-summary', required=True)
    parser.add_argument('--session-keys', required=True, help='comma-separated session keys')
    args = parser.parse_args()

    results = []
    for idx, session_key in enumerate([x for x in args.session_keys.split(',') if x], start=1):
        task_id = f"{args.task_id_prefix}-{idx:02d}"
        results.append(dispatch_one(session_key, args.project_id, task_id, args.pm_owner, args.file_path, args.request_summary))
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
