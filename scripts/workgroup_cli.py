#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
SHARED_ROOT = '/Volumes/Local Drawer/SharedProjects/'
ROLE_MAP_PATH = SKILL_ROOT / 'config' / 'team-role-map.json'


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, capture_output=True, text=True)


def load_role_map() -> dict:
    if ROLE_MAP_PATH.exists():
        return json.loads(ROLE_MAP_PATH.read_text(encoding='utf-8'))
    return {}


def route_pm_owner(task_type: str, need_finance: bool) -> dict:
    role_map = load_role_map()
    mapping = {
        'technical': 'technical',
        'web': 'technical',
        'development': 'technical',
        'miniprogram': 'technical',
        'research': 'research_analysis',
        'materials': 'research_analysis',
        'analysis': 'research_analysis',
        'reviewdraft': 'research_analysis',
        'writing': 'writing_integration',
        'expression': 'writing_integration',
        'external_materials': 'writing_integration',
        'budget': 'research_analysis',
        'finance': 'research_analysis',
        'commercial': 'research_analysis',
    }
    role_key = mapping.get(task_type.strip().lower())
    if not role_key:
        raise ValueError(f'unsupported task_type: {task_type}')
    pm_owner = role_map.get('project_managers', {}).get(role_key)
    finance_support = role_map.get('finance_support', []) if (need_finance or task_type in ('budget', 'finance', 'commercial')) else []
    assistants = []
    if role_key == 'research_analysis':
        assistants = ['coder']
    elif role_key == 'writing_integration':
        assistants = ['leon']
    return {
        'task_type': task_type,
        'pm_owner': pm_owner,
        'finance_support': finance_support,
        'assistants': assistants,
    }


def create_project(project_name: str, shortname: str, requester: str, pm_owner: str, assistants: list[str], finance_support: list[str]) -> dict:
    proc = run([
        'python3', str(SKILL_ROOT / 'scripts' / 'project_create.py'),
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


def dispatch_and_wait(session_key: str, project_id: str, task_id: str, pm_owner: str, file_path: str, request_summary: str, wait_seconds: int, poll_interval: int) -> dict:
    proc = run([
        'python3', str(SKILL_ROOT / 'scripts' / 'workgroup_run.py'),
        '--project-name', 'placeholder',
        '--shortname', 'placeholder',
        '--requester', 'placeholder',
        '--pm-owner', pm_owner,
        '--session-key', session_key,
        '--task-id', task_id,
        '--request-summary', request_summary,
        '--wait-seconds', str(wait_seconds),
        '--poll-interval', str(poll_interval),
        '--assistants', '',
        '--finance-support', '',
    ])
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or 'workgroup_run.py failed')
    return json.loads(proc.stdout)


def main() -> None:
    parser = argparse.ArgumentParser(description='A2A work group nxm - unified CLI entry')
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
    parser.add_argument('--pm-override', default='')
    parser.add_argument('--assistants-override', default='')
    args = parser.parse_args()

    routed = route_pm_owner(args.task_type, args.need_finance_support)
    pm_owner = args.pm_override or routed['pm_owner']
    assistants = [x for x in args.assistants_override.split(',') if x] or routed.get('assistants', [])
    finance_support = routed.get('finance_support', [])

    created = create_project(args.project_name, args.shortname, args.requester, pm_owner, assistants, finance_support)
    project_id = created['project_id']
    file_path = f'{SHARED_ROOT}{project_id}/'

    dispatched = dispatch_and_wait(
        session_key=args.session_key,
        project_id=project_id,
        task_id=args.task_id,
        pm_owner=pm_owner,
        file_path=file_path,
        request_summary=args.request_summary,
        wait_seconds=args.wait_seconds,
        poll_interval=args.poll_interval,
    )

    result = {
        'routing': routed,
        'created': created,
        'dispatch': dispatched,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
