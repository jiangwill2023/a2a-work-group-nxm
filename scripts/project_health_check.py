#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = [
    'README.md',
    'handoff.md',
    '00-brief/brief.md',
    '01-status/status.json',
    '01-status/next-step.md',
    '02-decisions/decision-log.md',
    '03-input',
    '04-working',
    '05-review',
    '06-final',
]


def main() -> None:
    parser = argparse.ArgumentParser(description='Check required project files/folders exist.')
    parser.add_argument('--project-root', required=True)
    args = parser.parse_args()
    root = Path(args.project_root)
    found, missing = [], []
    for rel in REQUIRED:
        p = root / rel
        if p.exists():
            found.append(rel)
        else:
            missing.append(rel)
    result = {
        'project_root': str(root),
        'status': 'OK' if not missing else 'MISSING_ITEMS',
        'found': found,
        'missing': missing,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
