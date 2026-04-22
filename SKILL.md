# A2A Work Group NXM

- version: v1.0.1
- date: 2026-04-22
- owner: OpenClaw Team
- status: public_ready
- purpose: Multi-agent collaboration skill supporting project creation, routing, dispatch, ACK tracking, and long-task checkpoint management.

---

## 1. Goal

Package proven team collaboration capabilities into a reusable skill:
- multi-agent organization and dispatch
- shared-directory project mainline management
- A2A broadcast / directed dispatch / ACK / BLOCKED / timeout / received
- PM and execution-role collaboration chains
- project templates and directory standardization
- long-task checkpoint advancement
- cross-session governance and permission management

---

## 2. Public Edition Notes

This public edition removes private identity traces:
- role placeholders instead of real team member names
- placeholders instead of real sender IDs, channel IDs, session keys
- configurable shared root instead of machine-specific path assumptions

Default roles:
- `COORDINATOR`
- `TECH_PM`
- `RESEARCH_PM`
- `WRITING_PM`
- `FINANCE_SUPPORT`
- `ASSISTANT_1`
- `ASSISTANT_2`

---

## 3. Core Scripts

- `project_create.py`
- `route_pm_owner.py`
- `workgroup_run.py`
- `workgroup_run_auto.py`
- `workgroup_cli.py`
- `dispatch_and_check.py`
- `ack_check.py`
- `retry_ack.py`
- `multi_dispatch.py`
- `project_health_check.py`
- `checkpoint_write.py`
- `system_deploy_sync.py` (optional/internal deployment helper)

---

## 4. Templates

- `templates/project-template/README.md`
- `templates/project-template/handoff.md`
- `templates/project-template/00-brief/brief.md`
- `templates/project-template/01-status/status.json`
- `templates/project-template/01-status/next-step.md`
- `templates/project-template/02-decisions/decision-log.md`

---

## 5. Key Rules

### project_id
- `p-YYYYMMDD-shortname`
- lowercase, english, digits, hyphen
- non-english project names should be converted before path creation

### shared root
- configured by user
- if path contains spaces, all script calls must use safe path handling

### receipt state layering
- `started` -> `timeout` -> `received` -> `ACKED/BLOCKED`
- `timeout` does not equal failure

### long tasks
- support `progress-log.md` checkpoint writing
- sync update `status.json`

### cross-session permissions
- agent-level `tools.allow` should include sessions tools
- `tools.sessions.visibility = all`
- if using Discord, elevated exec permission must be configured as needed

---

## 6. Config Files

- `config/team-role-map.example.json`
- `config/settings.example.json`
- `config/template-map.json`

Copy example configs before use.

---

## 7. Example Usage

```bash
python3 scripts/workgroup_cli.py \
  --project-name "sample project" \
  --shortname "sample-project" \
  --requester "USER" \
  --task-type "research" \
  --session-key "agent:PM_AGENT:discord:channel:CHANNEL_ID" \
  --task-id "task-20260422-01" \
  --request-summary "Please confirm project mainline and start work"
```

---

## 8. Next Steps

1. test against a fresh third-party environment
2. reduce remaining machine-specific assumptions in scripts
3. move internal docs to a private companion repo if needed
4. publish tagged release notes
