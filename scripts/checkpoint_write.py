#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
from pathlib import Path


def append_progress(project_root: Path, status: str, completed: str, current_focus: str, blockers: str, next_action: str, evidence_path: str, support_needed: str, updated_by: str) -> dict:
    progress_path = project_root / '01-status' / 'progress-log.md'
    block = f'''\n## checkpoint\n- status: {status}\n- completed_in_this_round: {completed}\n- current_focus: {current_focus}\n- blockers: {blockers}\n- next_action: {next_action}\n- evidence_path: {evidence_path}\n- support_needed: {support_needed}\n- updated_by: {updated_by}\n'''
    if progress_path.exists():
        existing = progress_path.read_text(encoding='utf-8')
    else:
        existing = '# progress log\n'
    progress_path.write_text(existing + block, encoding='utf-8')

    status_path = project_root / '01-status' / 'status.json'
    status_obj = json.loads(status_path.read_text(encoding='utf-8'))
    status_obj['status'] = status
    status_obj['latest_summary'] = completed
    status_obj['next_action'] = next_action
    status_obj['blockers'] = [] if not blockers or blockers == '-' else [blockers]
    status_obj['updated_by'] = updated_by
    status_path.write_text(json.dumps(status_obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    return {
        'project_root': str(project_root),
        'progress_log': str(progress_path),
        'status': status,
        'updated_by': updated_by,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description='Append a progress checkpoint to project mainline files.')
    parser.add_argument('--project-root', required=True)
    parser.add_argument('--status', required=True)
    parser.add_argument('--completed', required=True)
    parser.add_argument('--current-focus', required=True)
    parser.add_argument('--blockers', default='-')
    parser.add_argument('--next-action', required=True)
    parser.add_argument('--evidence-path', default='-')
    parser.add_argument('--support-needed', default='-')
    parser.add_argument('--updated-by', required=True)
    args = parser.parse_args()
    result = append_progress(
        project_root=Path(args.project_root),
        status=args.status,
        completed=args.completed,
        current_focus=args.current_focus,
        blockers=args.blockers,
        next_action=args.next_action,
        evidence_path=args.evidence_path,
        support_needed=args.support_needed,
        updated_by=args.updated_by,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
