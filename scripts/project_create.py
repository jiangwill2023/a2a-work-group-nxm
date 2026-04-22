#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

SETTINGS_PATH = Path('config/settings.json')
ROLE_MAP_PATH = Path('config/team-role-map.json')


def load_settings() -> dict:
    if SETTINGS_PATH.exists():
        return json.loads(SETTINGS_PATH.read_text(encoding='utf-8'))
    return {'shared_root': 'YOUR_SHARED_ROOT'}


def load_role_map() -> dict:
    if ROLE_MAP_PATH.exists():
        return json.loads(ROLE_MAP_PATH.read_text(encoding='utf-8'))
    return {
        'coordinator': 'COORDINATOR',
        'tech_lead': 'TECH_LEAD',
        'finance_support': ['FINANCE_SUPPORT'],
        'project_managers': {
            'technical': 'TECH_PM',
            'research_analysis': 'RESEARCH_PM',
            'writing_integration': 'WRITING_PM'
        }
    }


SHARED_ROOT = Path(load_settings().get('shared_root', 'YOUR_SHARED_ROOT'))
ALLOWED_STATUS = {'planning', 'ready', 'in_progress', 'review', 'blocked', 'done'}


def slugify_shortname(value: str) -> str:
    value = value.strip().lower()
    value = value.replace('_', '-')
    value = re.sub(r'[^a-z0-9\-\s]+', '-', value)
    value = re.sub(r'\s+', '-', value)
    value = re.sub(r'-+', '-', value).strip('-')
    return value


def require_english_lowercase(shortname: str) -> str:
    slug = slugify_shortname(shortname)
    if not slug:
        raise ValueError('shortname must resolve to a non-empty english lowercase slug')
    if re.search(r'[^a-z0-9\-]', slug):
        raise ValueError('shortname must use english lowercase letters, numbers, and hyphens only')
    return slug


def build_project_id(shortname: str, today: str | None = None) -> str:
    d = today or date.today().strftime('%Y%m%d')
    return f'p-{d}-{shortname}'


def ensure_dirs(project_root: Path) -> None:
    for rel in [
        '00-brief',
        '01-status',
        '02-decisions',
        '03-input',
        '04-working',
        '05-review',
        '06-final',
    ]:
        (project_root / rel).mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def render_readme(project_id: str) -> str:
    return f'''# project README

## purpose
说明本项目目录的用途、主线文件位置、协作规则与交接入口。

## root path
- project_root: {SHARED_ROOT}/{project_id}

## mainline files
- brief: `00-brief/brief.md`
- status: `01-status/status.json`
- next_step: `01-status/next-step.md`
- decision_log: `02-decisions/decision-log.md`

## folder guide
- `00-brief/`：项目简报与主线背景
- `01-status/`：当前状态、下一步、主线进度
- `02-decisions/`：关键决策、范围变化、路径调整
- `03-input/`：输入材料、外部资料、历史文件
- `04-working/`：工作草稿、分析过程、临时产物
- `05-review/`：待会审、待 review 版本
- `06-final/`：最终交付版本

## collaboration rules
- 正式推进优先以 `00-brief/`、`01-status/`、`02-decisions/` 为准
- 接手前先读主线文件
- 不要把 `04-working/` 草稿直接当最终结论
- 如发现文件不在共享根目录主线下，应标记为未挂主线并尽快迁回
'''


def render_handoff(project_id: str, pm_owner: str) -> str:
    return f'''# handoff

## project_id
- {project_id}

## current stage
- status: planning
- current_goal:
- current_focus:

## completed
- project folder initialized

## in_progress
-

## blockers
-

## next_owner
- pm_owner: {pm_owner}
- pm_support: []
- assistants: []

## next_actions
### next 1
- action:
- owner: {pm_owner}
- deliverable:
- done_definition:

### next 2
- action:
- owner: COORDINATOR
- deliverable:
- done_definition:

## do_not_repeat
- do not start execution without first checking shared-root mainline files

## important_paths
- shared_root: `{SHARED_ROOT}/`
- project_root: `{SHARED_ROOT}/{project_id}/`
- latest_output:

## handoff_note
-
'''


def render_brief(project_name: str, project_id: str, requester: str, pm_owner: str) -> str:
    return f'''# project brief

## 1. project basic info
- project_name: {project_name}
- project_id: {project_id}
- created_at: {date.today().isoformat()}
- requester: {requester}
- coordinator: COORDINATOR

## 2. project organization
- pm_owner: {pm_owner}
- pm_support: []
- assistants: []
- tech_lead: TECH_LEAD
- finance_support: []

## 3. project goal
请明确写清本项目最终要完成什么、交付什么、达成什么结果。

## 4. background
说明项目来源、上下文、已有进展、当前背景。

## 5. input materials
- links:
- files:
- history:
- references:
- notes:

## 6. output requirements
- deliverables:
- file_formats:
- delivery_path: {SHARED_ROOT}/{project_id}/
- review_required: yes
- external_send_required: no
- deadline:

## 7. work division
- owner_tasks:
- support_tasks:
- assistant_tasks:

## 8. current stage
- status: planning
- current_focus:
- current_blockers:

## 9. risks and notes
- risks:
- dependencies:
- special_requirements: all formal files stay under shared root mainline

## 10. latest updates
-
'''


def render_status(project_name: str, project_id: str, pm_owner: str) -> dict:
    status = {
        'project_name': project_name,
        'project_id': project_id,
        'coordinator': 'COORDINATOR',
        'pm_owner': pm_owner,
        'pm_support': [],
        'assistants': [],
        'tech_lead': 'TECH_LEAD',
        'finance_support': [],
        'status': 'planning',
        'current_task': '',
        'latest_output': 'project root initialized',
        'latest_summary': 'project created under shared-root governance',
        'blockers': [],
        'next_action': 'pm_owner reads mainline files and fills initial project details',
        'updated_at': date.today().isoformat(),
        'updated_by': 'COORDINATOR'
    }
    if status['status'] not in ALLOWED_STATUS:
        raise ValueError('invalid initial status')
    return status


def render_next_step(pm_owner: str) -> str:
    return f'''# next step

## current goal
完成项目初始化后的第一轮资料梳理与主线更新。

## current owner
- pm_owner: {pm_owner}
- pm_support: []
- assistants: []

## next 1
- action: read mainline files and fill initial project details
- owner: {pm_owner}
- deliverable: updated brief and status
- done_definition: brief and status reflect actual project scope and current focus

## next 2
- action: decide whether support roles or assistants are needed
- owner: COORDINATOR
- deliverable: dispatch decision
- done_definition: project organization is explicitly confirmed

## next 3
- action: organize initial materials into shared-root structure
- owner: {pm_owner}
- deliverable: initial input set
- done_definition: key source materials are placed or referenced under project root

## current blockers
-

## requester decisions needed
-
'''


def render_decision_log() -> str:
    return f'''# decision log

## usage
记录本项目中的关键决定、范围变化、路径调整、角色变化、输出变化。
每条记录尽量简明，便于后续 agent 接手时快速理解。

---

## record template
- time:
- recorded_by:
- topic:
- original_plan:
- new_decision:
- reason:
- impact:
- next_action:

---

## records

### record 001
- time: {date.today().isoformat()}
- recorded_by: COORDINATOR
- topic: project initialization
- original_plan: no shared-root project initialized yet
- new_decision: initialize project under shared root with standard template
- reason: follow team governance and shared-root rules
- impact: project now has a formal mainline location and required files
- next_action: pm_owner reads project files and continues work
'''


def create_project(project_name: str, shortname: str, requester: str, pm_owner: str, assistants: list[str] | None = None, finance_support: list[str] | None = None) -> dict:
    assistants = assistants or []
    finance_support = finance_support or []
    shortname = require_english_lowercase(shortname)
    project_id = build_project_id(shortname)
    project_root = SHARED_ROOT / project_id
    ensure_dirs(project_root)
    write_text(project_root / 'README.md', render_readme(project_id))
    write_text(project_root / 'handoff.md', render_handoff(project_id, pm_owner))
    brief = render_brief(project_name, project_id, requester, pm_owner)
    brief = brief.replace('- assistants: []', f'- assistants: {assistants}')
    brief = brief.replace('- finance_support: []', f'- finance_support: {finance_support}')
    write_text(project_root / '00-brief' / 'brief.md', brief)
    status_obj = render_status(project_name, project_id, pm_owner)
    status_obj['assistants'] = assistants
    status_obj['finance_support'] = finance_support
    write_text(project_root / '01-status' / 'status.json', json.dumps(status_obj, ensure_ascii=False, indent=2) + '\n')
    next_step = render_next_step(pm_owner)
    next_step = next_step.replace('- assistants: []', f'- assistants: {assistants}')
    write_text(project_root / '01-status' / 'next-step.md', next_step)
    write_text(project_root / '02-decisions' / 'decision-log.md', render_decision_log())
    return {
        'project_name': project_name,
        'project_id': project_id,
        'project_root': str(project_root),
        'pm_owner': pm_owner,
        'assistants': assistants,
        'finance_support': finance_support,
        'status': 'planning'
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Create a shared-root project with standard template files.')
    parser.add_argument('--project-name', required=True)
    parser.add_argument('--shortname', required=True, help='english lowercase shortname / slug')
    parser.add_argument('--requester', required=True)
    parser.add_argument('--pm-owner', required=True)
    parser.add_argument('--assistants', default='')
    parser.add_argument('--finance-support', default='')
    args = parser.parse_args()
    assistants = [x for x in args.assistants.split(',') if x]
    finance_support = [x for x in args.finance_support.split(',') if x]
    result = create_project(
        project_name=args.project_name,
        shortname=args.shortname,
        requester=args.requester,
        pm_owner=args.pm_owner,
        assistants=assistants,
        finance_support=finance_support,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
