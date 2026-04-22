# A2A work group nxm skill design v1

- date: 2026-04-21
- owner: qiang
- status: v1_executable
- purpose: 将当前团队协作制度沉淀为可复用的 `A2A work group nxm` skill 设计，已覆盖从立项到派单到回执到长任务推进的完整主链。

---

## 1. 目标

把当前已经验证过的能力组合成可复用技能：
- 多 agent 组织与派单
- 基于共享目录的项目主线管理
- A2A 广播 / 定向派单 / ACK / BLOCKED / timeout / received
- 项目经理与执行位的协作链
- 项目文件模板与目录标准化
- 长任务 checkpoint 推进
- 跨 session 工具修通与权限管理

这里的 `nxm` 指：
- `n` = 项目经理 / 协调位数量
- `m` = 执行位 / 支持位数量

目标不是只支持固定 1:1，而是支持小团队多角色协作。

---

## 2. 当前已具备能力

### A2A 链路
- `sessions.send` 可用于定向发送
- `sessions.get` 可用于 ACK / BLOCKED / timeout / received 回读
- 团队广播与项目经理派单已经实测成功
- 跨 session 发送已修通（根因：`tools.allow` + `tools.sessions.visibility = all`）

### 文件主线
- 已形成共享根目录默认值：`/Volumes/Local Drawer/SharedProjects/`
- 已形成标准项目模板目录与核心文件
- 已形成 `project_id`、`status`、`next-step`、`decision-log`、`progress-log` 规则
- 已支持 checkpoint 写入与长任务推进

### 组织结构
- `qiang`：总调度 / 总协调 / 收口
- `tracy`：技术 pm / 技术总监
- `mr-library`：资料分析 pm，管理 `coder`
- `may`：文稿整合 pm，管理 `leon`
- `steven`：财务支持

### 自动化脚本层
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

## 3. skill 应覆盖的模块

### module a: dispatch_router
根据任务类型决定：
- 是否立项
- 主责 pm 是谁
- 是否需要技术把关
- 是否需要财务支持
- 是否需要组临时项目小组
- 自动挂接 assistant / finance_support

### module b: project_initializer
负责：
- 生成 `project_id`
- 创建项目目录
- 初始化模板文件
- 写入初始 brief / status / next-step / decision-log
- 对共享盘路径中的空格进行安全处理（quoted path / safe path invocation）
- 自动写入 project organization（pm_owner / assistants / finance_support）

### module c: a2a_dispatch
负责：
- 团队广播
- 定向派单
- 携带 `project_id` / `task_id` / `file_path`
- 要求 `ACK / BLOCKED`
- 区分 `timeout`、`received`、`ACKED`、`BLOCKED` 的不同含义
- 支持 retry_ack 与多目标派单

### module d: status_governance
负责：
- 定义谁维护 `status.json`
- 哪些事件必须更新
- 哪些事件必须写 decision-log
- 长任务 checkpoint 写入规则
- `progress-log.md` 追加与 `status.json` 同步更新

### module e: handoff_control
负责：
- 接手前必读检查
- handoff 模板
- 交接回执格式
- 项目健康检查

### module f: escalation
负责：
- 技术升级给 `tracy`
- 分析升级给 `mr-library`
- 文稿升级给 `may`
- 商业判断升级给 `steven`
- 最终统筹升级给 `qiang`
- 执行助手失速时由 manager 先管，tech lead 把关

### module g: tool_policy
负责：
- 确保 agent-level `tools.allow` 包含 sessions 工具
- 确保 `tools.sessions.visibility = all`
- 确保 Discord 来源具备 elevated exec 权限
- 确保跨 session 发送不被权限层拦截

---

## 4. skill 的建议输入

建议 skill 接受至少这些输入：
- `project_name`
- `task_type`
- `goal`
- `requester`
- `materials`
- `deadline`
- `need_finance_support`
- `need_tech_review`
- `team_scope`
- `pm_override`（可选，覆盖默认路由）
- `assistants_override`（可选，覆盖默认 assistant 挂接）

---

## 5. skill 的建议输出

至少应输出：
- 建议 `pm_owner`
- 建议 `pm_support`
- 建议 `assistants`
- `project_id`
- `project_root`
- 初始化文件清单
- A2A 派单建议文案
- 下一步执行清单
- 回执状态跟踪入口

---

## 6. 分阶段演进建议

### phase 1：已完成
- 总规范
- project template
- handoff template
- 派单文案模板
- 项目创建脚本
- ACK 检查脚本
- 路径安全调用处理

### phase 2：已完成
- 自动路由脚本
- 自动派单与 ACK 等待
- retry_ack
- multi_dispatch
- project_health_check
- checkpoint_write
- system_deploy_sync

### phase 3：当前阶段
- 把路由、立项、文件初始化、派单、回执合成标准 skill 流程
- 形成可复用的 `A2A work group nxm` skill 封装
- 支持项目级角色覆盖（如 tracy pm + coder assistant）
- 支持长任务 checkpoint 与多断点推进

---

## 7. 当前结论

# `A2A work group nxm` 已经从规则草案进入可执行阶段，核心主链 create -> dispatch -> ack -> checkpoint 已跑通。

---

## 8. 实现经验（截至 2026-04-21）

### 共享根目录
- `/Volumes/Local Drawer/SharedProjects/`
- 路径含空格，所有脚本调用必须统一做 quoted path / safe path 处理

### 跨 session 发送修通
- 根因 1：`tools.allow` 太窄，agent 层缺 sessions 工具
- 根因 2：`tools.sessions.visibility` 不是 `all`
- 修复方式：给所有 agent 补 sessions 工具 + 设置 `visibility = all`

### elevated exec 权限
- Discord 来源需要 `tools.elevated.enabled = true`
- 需要 `tools.elevated.allowFrom.discord` 包含授权 sender
- 各 agent 也需要同步开启

### 回执状态分层
- `started` -> `timeout` -> `received` -> `ACKED/BLOCKED`
- `timeout` 不等于失败
- 后续证据确认已收到时，应更新为 `received`

### 长任务机制
- 不适合要求“立刻 ACK + 立刻做完”
- 应支持 `progress-log.md` checkpoint 写入
- `status.json` 应同步更新

### 项目级角色覆盖
- 默认路由可被项目级覆盖
- 例如 tracy 做 pm、coder 做 assistant，不强制按默认 manager 归属

---

## 9. 下一步建议

1. 形成 `workgroup_run_auto` 的 skill 封装入口
2. 把 `team-role-map.json` 纳入 skill 配置
3. 支持项目模板自动选择与自定义
4. 支持多项目并发治理
5. 支持异常项目自动标记与巡检
6. 最终形成可开源的 `A2A work group nxm` skill 包
