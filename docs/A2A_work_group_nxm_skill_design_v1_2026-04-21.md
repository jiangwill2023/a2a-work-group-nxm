# A2A Work Group NXM Skill Design v1

- date: 2026-04-21
- owner: OWNER
- status: v1_executable
- purpose: Standardized multi-agent collaboration skill covering project creation, dispatch, ACK tracking, and long-task checkpoint management.

---

## 1. Goal

Combine verified capabilities into a reusable skill:
- Multi-agent organization and dispatch
- Shared directory-based project mainline management
- A2A broadcast / directed dispatch / ACK / BLOCKED / timeout / received
- PM and execution role collaboration chains
- Project file templates and directory standardization
- Long-task checkpoint advancement
- Cross-session tool governance and permission management

Here `nxm` means:
- `n` = number of project managers / coordinators
- `m` = number of execution / support roles

Goal is not fixed 1:1, but supporting small team multi-role collaboration.

---

## 2. Current Capabilities

### A2A Link
- `sessions.send` for directed sending
- `sessions.get` for ACK / BLOCKED / timeout / received reading
- Team broadcast and PM dispatch verified
- Cross-session sending fixed (root cause: `tools.allow` + `tools.sessions.visibility = all`)

### File Mainline
- Shared root default: `YOUR_SHARED_ROOT` (configure in settings.json)
- Standard project template directories and core files
- `project_id`, `status`, `next-step`, `decision-log`, `progress-log` rules
- Checkpoint writing and long-task advancement supported

### Organization Structure
- `COORDINATOR`: Overall dispatch / coordination / closure
- `TECH_PM`: Technical PM / technical director
- `RESEARCH_PM`: Research analysis PM, manages `ASSISTANT_1`
- `WRITING_PM`: Document integration PM, manages `ASSISTANT_2`
- `FINANCE_SUPPORT`: Financial support

### Automation Script Layer
- `project_create.py`
- `ack_check.py`
- `dispatch_and_check.py`
- `workgroup_run.py`
- `route_pm_owner.py`
- `workgroup_run_auto.py`
- `retry_ack.py`
- `multi_dispatch.py`
- `project_health_check.py`
- `checkpoint_write.py`
- `system_deploy_sync.py`

---

## 3. Skill Modules

### Module A: Dispatch Router
Decides based on task type:
- Whether to establish project
- Primary PM
- Whether technical oversight needed
- Whether finance support needed
- Whether to form temporary project team
- Auto-attach assistant / finance_support

### Module B: Project Initializer
Responsible for:
- Generating `project_id`
- Creating project directory
- Initializing template files
- Writing initial brief / status / next-step / decision-log
- Safe handling of spaces in shared disk paths (quoted path / safe path invocation)
- Auto-writing project organization (pm_owner / assistants / finance_support)

### Module C: A2A Dispatch
Responsible for:
- Team broadcast
- Directed dispatch
- Carrying `project_id` / `task_id` / `file_path`
- Requiring `ACK / BLOCKED`
- Distinguishing `timeout`, `received`, `ACKED`, `BLOCKED`
- Supporting retry_ack and multi-target dispatch

### Module D: Status Governance
Responsible for:
- Defining who maintains `status.json`
- Which events must update
- Which events must write decision-log
- Long-task checkpoint writing rules
- `progress-log.md` append and `status.json` sync update

### Module E: Handoff Control
Responsible for:
- Pre-handoff required reading check
- Handoff template
- Handoff receipt format
- Project health check

### Module F: Escalation
Responsible for:
- Technical escalation to `TECH_PM`
- Analysis escalation to `RESEARCH_PM`
- Document escalation to `WRITING_PM`
- Business judgment escalation to `FINANCE_SUPPORT`
- Final coordination escalation to `COORDINATOR`
- Execution assistant slowdown handled by manager first, tech lead oversees

### Module G: Tool Policy
Responsible for:
- Ensuring agent-level `tools.allow` includes sessions tools
- Ensuring `tools.sessions.visibility = all`
- Ensuring Discord source has elevated exec permission
- Ensuring cross-session sending not blocked by permission layer

---

## 4. Skill Inputs

Skill should accept at least:
- `project_name`
- `task_type`
- `goal`
- `requester`
- `materials`
- `deadline`
- `need_finance_support`
- `need_tech_review`
- `team_scope`
- `pm_override` (optional, overrides default routing)
- `assistants_override` (optional, overrides default assistant attachment)

---

## 5. Skill Outputs

Should output at least:
- Suggested `pm_owner`
- Suggested `pm_support`
- Suggested `assistants`
- `project_id`
- `project_root`
- Initialized file list
- A2A dispatch suggested copy
- Next step execution list
- Receipt status tracking entry

---

## 6. Phase Evolution

### Phase 1: Completed
- General specifications
- Project template
- Handoff template
- Dispatch copy template
- Project creation scripts
- ACK check scripts
- Path safety handling

### Phase 2: Completed
- Automatic routing scripts
- Automatic dispatch and ACK waiting
- retry_ack
- multi_dispatch
- project_health_check
- checkpoint_write
- system_deploy_sync

### Phase 3: Current
- Combine routing, creation, file init, dispatch, receipt into standard skill flow
- Form reusable `A2A work group nxm` skill packaging
- Support project-level role overrides (e.g., TECH_PM as PM + ASSISTANT_1 as assistant)
- Support long-task checkpoint and multi-breakpoint advancement

---

## 7. Conclusion

# `A2A work group nxm` has moved from specification draft to executable stage. Core mainline create -> dispatch -> ack -> checkpoint is operational.

---

## 8. Implementation Experience (As of 2026-04-21)

### Shared Root Directory
- `YOUR_SHARED_ROOT` (configure in settings.json)
- Path contains spaces, all script calls must uniformly do quoted path / safe path handling

### Cross-Session Sending Fix
- Root cause 1: `tools.allow` too narrow, agent layer missing sessions tools
- Root cause 2: `tools.sessions.visibility` not `all`
- Fix: Add sessions tools to all agents + set `visibility = all`

### Elevated Exec Permission
- Discord source needs `tools.elevated.enabled = true`
- Needs `tools.elevated.allowFrom.discord` containing authorized sender
- Each agent also needs synchronous enablement

### Receipt Status Layering
- `started` -> `timeout` -> `received` -> `ACKED/BLOCKED`
- `timeout` does not equal failure
- When subsequent evidence confirms received, update to `received`

### Long-Task Mechanism
- Not suitable to require "immediate ACK + immediate completion"
- Should support `progress-log.md` checkpoint writing
- `status.json` should sync update

### Project-Level Role Override
- Default routing can be overridden at project level
- E.g., TECH_PM as PM, ASSISTANT_1 as assistant, not forced by default manager affiliation

---

## 9. Next Steps

1. Form `workgroup_run_auto` skill packaging entry
2. Incorporate `team-role-map.json` into skill config
3. Support automatic project template selection and customization
4. Support multi-project concurrent governance
5. Support automatic exception project flagging and inspection
6. Finalize open-source `A2A work group nxm` skill package
