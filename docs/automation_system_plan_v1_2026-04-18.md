# Automation System Plan v1

- date: 2026-04-18
- owner: OWNER
- status: in_progress
- objective: Build an automated team collaboration system based on shared directories, A2A communication, and project templates.

---

## 1. Overall Goal

Build an automated team operation system with:
- Shared root directory as the mainline
- A2A as the collaboration channel
- Project templates and status files as governance foundation

---

## 2. Current Foundation

- coordinator: `COORDINATOR`
- pm roles: `TECH_PM`, `RESEARCH_PM`, `WRITING_PM`
- assistants: `ASSISTANT_1`, `ASSISTANT_2`
- finance support: `FINANCE_SUPPORT`
- shared root: `/Volumes/Local Drawer/SharedProjects/`
- project_id rule: `p-YYYYMMDD-shortname`
- path naming rule: all persisted project paths / folder names / shortnames must use english lowercase
- required files:
  - `00-brief/brief.md`
  - `01-status/status.json`
  - `01-status/next-step.md`
  - `02-decisions/decision-log.md`
  - `README.md`
  - `handoff.md`

---

## 3. Automation Layers

### Layer 1: Standardization
- General specifications
- Templates
- Naming rules
- Shared directory structure

### Layer 2: Scripts
- Project creation
- Task dispatch
- ACK checking
- Path safety handling

### Layer 3: Skill Packaging
- Route + initialize + dispatch + ACK as standard skill flow
- Support for role overrides
- Support for long-task checkpoints

---

## 4. Implementation Status

### Completed
- [x] Team specifications
- [x] Project templates
- [x] Dispatch templates
- [x] Project creation scripts
- [x] ACK check scripts
- [x] Path safety handling

### In Progress
- [ ] Automatic routing scripts
- [ ] Automatic dispatch and ACK waiting
- [ ] retry_ack
- [ ] multi_dispatch
- [ ] project_health_check
- [ ] checkpoint_write
- [ ] system_deploy_sync

### Next Steps
1. Form skill packaging entry
2. Incorporate team-role-map into skill config
3. Support automatic template selection
4. Support multi-project concurrent governance
5. Support automatic flagging for exception projects
6. Finalize open-source skill package
