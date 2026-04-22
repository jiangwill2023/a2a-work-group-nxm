#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess
from typing import Any


def load_session(session_key: str) -> dict[str, Any]:
    proc = subprocess.run(
        ['openclaw', 'gateway', 'call', 'sessions.get', '--json', '--params', json.dumps({'key': session_key}, ensure_ascii=False)],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'sessions.get failed')
    return json.loads(proc.stdout)


def extract_text(msg: dict[str, Any]) -> str:
    parts = []
    for item in msg.get('content', []):
        if item.get('type') == 'text':
            parts.append(item.get('text', ''))
    return '\n'.join(parts).strip()


def check_task(session_data: dict[str, Any], task_id: str) -> dict[str, Any]:
    messages = session_data.get('messages', [])
    task_index = None
    task_seq = None
    for i, msg in enumerate(messages):
        if msg.get('role') != 'user':
            continue
        text = extract_text(msg)
        if task_id in text:
            task_index = i
            task_seq = msg.get('__openclaw', {}).get('seq')
    if task_index is None:
        return {
            'task_id': task_id,
            'status': 'TASK_ID_NOT_FOUND',
            'task_seq': None,
            'reply_seq': None,
            'evidence': ''
        }

    for msg in messages[task_index + 1: task_index + 8]:
        if msg.get('role') != 'assistant':
            continue
        text = extract_text(msg)
        seq = msg.get('__openclaw', {}).get('seq')
        stripped = text.strip()
        if stripped == 'ACK':
            return {
                'task_id': task_id,
                'status': 'ACKED',
                'task_seq': task_seq,
                'reply_seq': seq,
                'evidence': text
            }
        if stripped.startswith('BLOCKED') or 'exact blocker' in stripped.lower():
            return {
                'task_id': task_id,
                'status': 'BLOCKED',
                'task_seq': task_seq,
                'reply_seq': seq,
                'evidence': text
            }
        if stripped:
            return {
                'task_id': task_id,
                'status': 'IN_PROGRESS',
                'task_seq': task_seq,
                'reply_seq': seq,
                'evidence': text[:500]
            }

    return {
        'task_id': task_id,
        'status': 'IN_PROGRESS',
        'task_seq': task_seq,
        'reply_seq': None,
        'evidence': ''
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Check ACK / BLOCKED status for a task_id in a session.')
    parser.add_argument('--session-key', required=True)
    parser.add_argument('--task-id', required=True)
    args = parser.parse_args()

    session_data = load_session(args.session_key)
    result = check_task(session_data, args.task_id)
    result['session_key'] = args.session_key
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
