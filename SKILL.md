# A2A work group nxm

- version: v1
- date: 2026-04-21
- owner: qiang
- status: executable
- purpose: 多 agent 协作 skill，支持从立项到派单到回执到长任务推进的完整主链。

---

## 1. 目标

把当前已验证的团队协作能力封装为可复用 skill：
- 多 agent 组织与派单
- 基于共享目录的项目主线管理
- A2A 广播 / 定向派单 / ACK / BLOCKED / timeout / received
- 项目经理与执行位的协作链
- 项目文件模板与目录标准化
- 长任务 checkpoint 推进
- 跨 session 工具权限管理

---

## 2. 组织结构

- `qiang`：总调度 / 总协调 / 收口
- `tracy`：技术 pm / 技术总监
- `mr-library`：资料分析 pm，管理 `coder`
- `may`：文稿整合 pm，管理 `leon`
- `steven`：财务支持

---

## 3. 核心脚本

| 脚本 | 用途 |
|------|------|
| `project_create.py` | 创建项目目录与初始文件 |
| `route_pm_owner.py` | 按任务类型自动路由 pm_owner |
| `workgroup_run.py` | 端到端主链：创建 -> 派单 -> 等 ACK |
| `workgroup_run_auto.py` | 自动路由版端到端主链 |
| `dispatch_and_check.py` | 发派单并检查 ACK |
| `ack_check.py` | 按 task_id 精准检查 ACK/BLOCKED |
| `retry_ack.py` | 超时窗口内重试 ACK 检查 |
| `multi_dispatch.py` | 同一任务多目标派单 |
| `project_health_check.py` | 检查项目主线结构完整性 |
| `checkpoint_write.py` | 写入 progress checkpoint 并同步 status |
| `system_deploy_sync.py` | 同步系统脚本与文档到部署区 |

---

## 4. 模板

| 模板 | 用途 |
|------|------|
| `project-template/README.md` | 项目根目录说明 |
| `project-template/handoff.md` | 交接模板 |
| `project-template/00-brief/brief.md` | 项目简报 |
| `project-template/01-status/status.json` | 项目状态 |
| `project-template/01-status/next-step.md` | 下一步 |
| `project-template/02-decisions/decision-log.md` | 决策日志 |

---

## 5. 关键规则

### project_id
- `p-YYYYMMDD-shortname`
- 全小写、英文、数字、连字符
- 中文项目名需先转英文 shortname

### 共享根目录
- `/Volumes/Local Drawer/SharedProjects/`
- 路径含空格，所有脚本调用必须做 quoted path 处理

### 回执状态分层
- `started` -> `timeout` -> `received` -> `ACKED/BLOCKED`
- `timeout` 不等于失败

### 长任务
- 支持 `progress-log.md` checkpoint 写入
- `status.json` 同步更新

### 跨 session 权限
- agent-level `tools.allow` 需包含 sessions 工具
- `tools.sessions.visibility = all`
- Discord 来源需开启 elevated exec

---

## 6. 使用示例

### 创建项目并自动路由
```bash
python3 workgroup_run_auto.py \
  --project-name "sample project" \
  --shortname "sample-project" \
  --requester "will" \
  --task-type "research" \
  --session-key "agent:mr-library:discord:channel:1480155817952153651" \
  --task-id "sample-20260421-01" \
  --request-summary "please confirm project mainline and start work" \
  --wait-seconds 30 \
  --poll-interval 5
```

### 写入 checkpoint
```bash
python3 checkpoint_write.py \
  --project-root "/Volumes/Local Drawer/SharedProjects/p-20260421-sample-project" \
  --status "in_progress" \
  --completed "initial setup done" \
  --current-focus "continue mapping" \
  --next-action "update brief and status" \
  --updated-by "qiang"
```

---

## 7. 下一步

1. 形成更完整的 skill 封装入口
2. 把 `team-role-map.json` 纳入 skill 配置
3. 支持项目模板自动选择与自定义
4. 支持多项目并发治理
5. 支持异常项目自动标记与巡检
6. 最终形成可开源的 skill 包
