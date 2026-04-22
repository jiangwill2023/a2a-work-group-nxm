# a2a dispatch template

```text
project_id=<project_id>
task_id=<task_id>
pm_owner=<pm_owner>
file_path=/Volumes/Local Drawer/SharedProjects/<project_id>/
request_summary=<one-line summary>
expected_reply=ACK|BLOCKED

请先读取以下主线文件：
- 00-brief/brief.md
- 01-status/status.json
- 01-status/next-step.md
- 如有必要，再读取 02-decisions/decision-log.md

请基于项目文件继续执行，不要脱离共享目录主线。
如可执行，请仅回复 ACK。
如无法执行，请仅回复 BLOCKED，并说明 exact blocker。
```
