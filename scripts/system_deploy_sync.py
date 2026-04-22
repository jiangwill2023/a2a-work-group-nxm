#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from pathlib import Path
import shutil

SRC = Path('/Users/admin-ai/.openclaw/workspace-qiang')
DEST = Path('/Volumes/Local Drawer/SharedProjects/_system')

SCRIPTS = [
    'project_create.py', 'ack_check.py', 'dispatch_and_check.py', 'workgroup_run.py',
    'route_pm_owner.py', 'workgroup_run_auto.py', 'retry_ack.py', 'multi_dispatch.py', 'project_health_check.py'
]
DOCS = [
    '团队协作总规范_v2_草案_2026-04-18.md', '自动化运行系统计划_v1_2026-04-18.md',
    'a2a_dispatch_template.md', 'ack_check_sop.md', 'shared-projects-bootstrap.md',
    'team-role-map.json', 'A2A_work_group_nxm_skill_design_v0.1_2026-04-18.md', 'handoff_checklist.md'
]


def sync():
    (DEST / 'scripts').mkdir(parents=True, exist_ok=True)
    (DEST / 'docs').mkdir(parents=True, exist_ok=True)
    for name in SCRIPTS:
        shutil.copy2(SRC / name, DEST / 'scripts' / name)
    for name in DOCS:
        shutil.copy2(SRC / name, DEST / 'docs' / name)
    print(DEST)


if __name__ == '__main__':
    sync()
