# A2A Work Group NXM

Multi-agent collaboration skill for OpenClaw. Supports project initialization, dispatch, ACK tracking, and long-task checkpoint management.

## Overview

This skill enables small teams of AI agents to collaborate on projects through:
- **Automatic project routing** based on task type
- **Standardized project directories** with templates
- **A2A dispatch** with ACK/BLOCKED tracking
- **Long-task checkpoint** management
- **Cross-session communication** governance

## Quick Start

```bash
# Install to OpenClaw skills directory
cp -r a2a-work-group-nxm ~/.openclaw/skills/

# Create and dispatch a project
python3 ~/.openclaw/skills/a2a-work-group-nxm/scripts/workgroup_cli.py \
  --project-name "Market Research" \
  --shortname "market-research" \
  --requester "will" \
  --task-type "research" \
  --session-key "agent:mr-library:discord:channel:YOUR_CHANNEL" \
  --task-id "mr-20260421-01" \
  --request-summary "Please analyze market trends and prepare a brief"
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
- ACK/BLOCKED/timeout/received status tracking
- Retry mechanism for pending tasks
- Multi-target dispatch support

### Project Governance
- `status.json` with standardized states
- `decision-log.md` for key decisions
- `progress-log.md` for checkpoint updates
- Health check for project structure integrity

## Directory Structure

```
a2a-work-group-nxm/
├── skill.json              # Skill metadata
├── SKILL.md                # Skill documentation
├── INSTALL.md              # Installation guide
├── LICENSE                 # MIT License
├── README.md               # This file
├── config/
│   ├── team-role-map.json  # Team role configuration
│   └── template-map.json   # Project template selection
├── scripts/
│   ├── workgroup_cli.py    # Unified CLI entry
│   ├── workgroup_run.py    # End-to-end workflow
│   ├── project_create.py   # Project initialization
│   ├── route_pm_owner.py   # Task routing
│   ├── dispatch_and_check.py
│   ├── ack_check.py
│   ├── retry_ack.py
│   ├── multi_dispatch.py
│   ├── project_health_check.py
│   ├── checkpoint_write.py
│   └── system_deploy_sync.py
├── templates/
│   └── project-template/   # Standard project template
└── docs/
    └── *.md                # Documentation and SOPs
```

## Configuration

### Team Role Map
Edit `config/team-role-map.json` to customize your team:

```json
{
  "project_managers": {
    "technical": "tracy",
    "research_analysis": "mr-library",
    "writing_integration": "may"
  },
  "finance_support": ["steven"],
  "tech_lead": "tracy",
  "coordinator": "qiang"
}
```

### Template Selection
Choose templates via `config/template-map.json`:
- `standard`: Full template with all governance files
- `minimal`: Brief + status + next-step only
- `full`: Standard + additional governance

## Task Types

| Type | PM | Assistants |
|------|-----|-----------|
| research, materials, analysis | mr-library | coder |
| writing, expression | may | leon |
| technical, web, development | tracy | - |
| budget, finance, commercial | mr-library + steven | - |

## Requirements

- Python >= 3.9
- OpenClaw >= 2026.4.15
- Shared project root directory (default: `/Volumes/Local Drawer/SharedProjects/`)

## Permissions

This skill requires:
- `sessions.send`
- `sessions.get`
- `sessions.list`
- `exec`
- `read`
- `write`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

## License

MIT License - see [LICENSE](LICENSE)

## Author

- **WillQ** - Initial design and implementation
- **OpenClaw Team** - Testing and feedback

## Acknowledgments

Built for the OpenClaw multi-agent collaboration ecosystem.
