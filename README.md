# A2A Work Group NXM

Multi-agent collaboration skill for OpenClaw. Supports project initialization, routing, A2A dispatch, ACK tracking, and long-task checkpoint management.

## Overview

This skill helps small teams of AI agents collaborate through:
- Automatic project routing based on task type
- Standardized project directories with templates
- A2A dispatch with ACK / BLOCKED / timeout / received tracking
- Long-task checkpoint management
- Cross-session communication governance

## Public-Ready Notes

This repository is the standardized public edition.
- Real team member names have been replaced by role placeholders
- Real sender IDs, channel IDs, and session keys have been removed
- Machine-specific paths have been replaced with configurable placeholders
- Example configuration files are provided in `config/*.example.json`

## Quick Start

```bash
# install
cp -r a2a-work-group-nxm ~/.openclaw/skills/

# copy example config
cp config/team-role-map.example.json config/team-role-map.json
cp config/settings.example.json config/settings.json

# run
python3 ~/.openclaw/skills/a2a-work-group-nxm/scripts/workgroup_cli.py \
  --project-name "Market Research" \
  --shortname "market-research" \
  --requester "USER" \
  --task-type "research" \
  --session-key "agent:PM_AGENT:discord:channel:CHANNEL_ID" \
  --task-id "task-20260422-01" \
  --request-summary "Analyze market trends and prepare a brief"
```

## Features

### Project Initialization
- Automatic `project_id` generation (`p-YYYYMMDD-shortname`)
- Standard directory structure with templates
- Role assignment (PM, assistants, finance support)

### Task Routing
- Automatic PM assignment based on task type
- Support for overrides (`--pm-override`, `--assistants-override`)
- Finance support auto-detection for budget/commercial tasks

### A2A Communication
- Team broadcast and directed dispatch
- ACK / BLOCKED / timeout / received tracking
- Retry mechanism for pending tasks
- Multi-target dispatch support

### Project Governance
- `status.json` with standardized states
- `decision-log.md` for key decisions
- `progress-log.md` for checkpoint updates
- Health check for project structure integrity

## Directory Structure

```text
a2a-work-group-nxm/
├── skill.json
├── SKILL.md
├── INSTALL.md
├── LICENSE
├── README.md
├── config/
│   ├── team-role-map.example.json
│   ├── team-role-map.json
│   ├── settings.example.json
│   └── template-map.json
├── scripts/
├── templates/
└── docs/
```

## Role Model

Default public placeholders:
- `COORDINATOR`
- `TECH_PM`
- `RESEARCH_PM`
- `WRITING_PM`
- `FINANCE_SUPPORT`
- `ASSISTANT_1`
- `ASSISTANT_2`

## Configuration

### Team Role Map
Use `config/team-role-map.example.json` as your starting point.

### Settings
Use `config/settings.example.json` to define:
- `shared_root`
- default template
- authorized senders
- session visibility

## Task Types

| Type | PM | Assistants |
|------|----|-----------|
| research, materials, analysis | RESEARCH_PM | ASSISTANT_1 |
| writing, expression | WRITING_PM | ASSISTANT_2 |
| technical, web, development | TECH_PM | - |
| budget, finance, commercial | RESEARCH_PM + FINANCE_SUPPORT | - |

## Requirements

- Python >= 3.9
- OpenClaw >= 2026.4.15
- Configured shared project root

## Permissions

This skill requires:
- `sessions.send`
- `sessions.get`
- `sessions.list`
- `exec`
- `read`
- `write`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT License - see [LICENSE](LICENSE).

## Maintainer

OpenClaw Team
