#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROLE_MAP_PATH = Path('team-role-map.json')

TASK_TYPE_TO_ROLE = {
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


def load_role_map() -> dict:
    return json.loads(ROLE_MAP_PATH.read_text(encoding='utf-8'))


def route_pm_owner(task_type: str, need_finance_support: bool) -> dict:
    role_map = load_role_map()
    task_type = task_type.strip().lower()
    role_key = TASK_TYPE_TO_ROLE.get(task_type)
    if not role_key:
        raise ValueError(f'unsupported task_type: {task_type}')
    pm_owner = role_map['project_managers'][role_key]
    finance_support = role_map.get('finance_support', []) if need_finance_support or task_type in ('budget', 'finance', 'commercial') else []
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


def main() -> None:
    parser = argparse.ArgumentParser(description='Route pm_owner by task type.')
    parser.add_argument('--task-type', required=True)
    parser.add_argument('--need-finance-support', action='store_true')
    args = parser.parse_args()
    result = route_pm_owner(args.task_type, args.need_finance_support)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
