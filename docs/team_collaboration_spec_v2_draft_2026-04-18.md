# Team Collaboration General Specification v2 Draft

- date: 2026-04-18
- coordinator: COORDINATOR
- status: draft_ready
- scope: Team organization, dispatch system, shared directory, project files, A2A collaboration, receipt and handoff rules

---

## 1. Overall Role Definitions

### Coordinator
- `COORDINATOR`
- Responsible for receiving user tasks, judging task types, assigning primary PM, organizing collaboration, maintaining shared directory order, tracking overall project progress, handoff and closure.

### Project Managers / Support Roles
- `TECH_PM`: Project manager, also technical director; responsible for technical projects, technical support, technical oversight.
- `RESEARCH_PM`: Project manager; responsible for research, materials, analysis, review drafts, and managing `ASSISTANT_1`.
- `WRITING_PM`: Project manager; responsible for document integration, expression optimization, and managing `ASSISTANT_2`.
- `FINANCE_SUPPORT`: Financial support; responsible for budget, estimation, cost and business judgment support.

### Execution Assistants
- `ASSISTANT_1`: Technical execution assistant, default managed by `RESEARCH_PM`, technical requirements overseen by `TECH_LEAD`.
- `ASSISTANT_2`: Development execution assistant, default managed by `WRITING_PM`, technical requirements overseen by `TECH_LEAD`.

---

## 2. Dispatch Principles

- Research, materials, analysis, review draft tasks priority to `RESEARCH_PM`
- Document integration, expression optimization, external materials tasks priority to `WRITING_PM`
- Web, mini-program, development, technical calibration tasks priority to `TECH_PM`
- When involving budget, profit, cost, business judgment, actively pull `FINANCE_SUPPORT` to participate
- If project needs multi-person collaboration, `COORDINATOR` responsible for forming temporary project team and clarifying primary and collaboration relationships

---

## 3. Collaboration Principles

- Language responsible for initiating and collaborating
- Files responsible for memory and landing
- All projects must establish project folders in shared directory
- All key task information must be written to project files
- A2A responsible for initiating and notifying
- Files responsible for task acceptance, decision recording, progress recording, evidence preservation
- Not allowed to have only chat without files
- Not allowed to have only files without current status receipt
- After each dispatch, subsequent promotion should quickly fall to corresponding project folder

---

## 4. Receipt Judgment Rules

- `started` = initiated, not equal to closed loop
- `timeout` = no immediate receipt in current waiting window, not equal to failure
- `received` = subsequent evidence confirmed received, but not yet proven `ACK / BLOCKED / executed`
- `ACK` = received, confirmed
- `BLOCKED` = received but cannot execute, need explicit explanation of blockage
- Not allowed to directly misreport `timeout` as failure; if subsequent confirmation received, should correct to `received`

---

## 5. Project File Rules

### status.json Must Update Triggers
- Phase switching
- Blocker appearing
- New deliverable forming
- Review conclusion forming
- Project pause / completion

### decision-log.md Must Update Triggers
- Scope change
- Deadline change
- Primary role change
- Output change
- Technical route change
- User proposes new key requirements
- After blocked, change to new path

---

## 6. A2A and Project File Combination Rules

- A2A messages responsible for initiating, notifying, ACK, BLOCKED
- Project files responsible for task acceptance, decision recording, progress recording, evidence preservation
- Not allowed to have only chat without files
- Not allowed to have only files without current status receipt
- After each dispatch, subsequent promotion should quickly fall to corresponding project folder

### Formal Dispatch Suggested Fields
Each formal dispatch suggestion should at least include:
- `project_id`
- `task_id`
- `pm_owner`
- `file_path`
- `expected_reply`

Recommended format:

```text
project_id=<project_id>
task_id=<task_id>
file_path=YOUR_SHARED_ROOT/<project_id>/
Please read project files first, then execute.
Please only reply ACK or BLOCKED.
```

---

## 7. Project Creation SOP (Standard Process)

From next project, execute in following order:
1. `COORDINATOR` judges whether to establish project
2. Generate `project_id`
3. Create project directory
4. Initialize template files
5. Write initial brief / status / next-step / decision-log
6. A2A dispatch to PM
7. Wait for ACK
8. If BLOCKED, record reason and escalate

---

## 8. Handoff Rules

- Before taking over, must read mainline files
- After taking over, must structured receipt
- Handoff must include: completed, current focus, next action, blockers
- Handoff template see `templates/project-template/handoff.md`

---

## 9. Exception Escalation

- Technical issues -> `TECH_PM`
- Materials analysis issues -> `RESEARCH_PM`
- Document issues -> `WRITING_PM`
- Business judgment issues -> `FINANCE_SUPPORT`
- Overall coordination issues -> `COORDINATOR`

---

## 10. Naming Rules

- All agent names lowercase
- All field names lowercase
- Status values lowercase and limited to: `planning`, `ready`, `in_progress`, `review`, `blocked`, `done`
- Shared root directory is user-configurable: `YOUR_SHARED_ROOT`
- Project folder name = `project_id`
- Chinese project names must convert to English shortname before landing
- Formal promotion based on `00-brief/`, `01-status/`, `02-decisions/`
- Before taking over, must read mainline files and structured receipt
- Exception escalation: technical->`TECH_PM`; materials analysis->`RESEARCH_PM`; documents->`WRITING_PM`; finance->`FINANCE_SUPPORT`; coordination->`COORDINATOR`
