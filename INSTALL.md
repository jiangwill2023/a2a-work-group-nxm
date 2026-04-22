# A2A Work Group NXM - Installation Guide

## Installation

### Method 1: Direct Copy
```bash
cp -r a2a-work-group-nxm ~/.openclaw/skills/
```

### Method 2: OpenClaw CLI (Future)
```bash
openclaw skills install a2a-work-group-nxm
```

## First-Time Setup
```bash
cp config/team-role-map.example.json config/team-role-map.json
cp config/settings.example.json config/settings.json
```

## Verification
```bash
python3 ~/.openclaw/skills/a2a-work-group-nxm/scripts/workgroup_cli.py \
  --project-name "test" \
  --shortname "test" \
  --requester "USER" \
  --task-type "research" \
  --session-key "agent:PM_AGENT:discord:channel:CHANNEL_ID" \
  --task-id "test-20260422-01" \
  --request-summary "test installation"
```

## Requirements
- Python >= 3.9
- OpenClaw >= 2026.4.15
- Shared root directory configured by user

## Configuration
- `config/team-role-map.json`: Team role mapping
- `config/settings.json`: Local settings
- `config/template-map.json`: Template selection
- `skill.json`: Skill metadata

## Permissions Required
- `sessions.send`
- `sessions.get`
- `sessions.list`
- `exec`
- `read`
- `write`
