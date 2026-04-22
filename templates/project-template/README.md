# project README

## purpose
说明本项目目录的用途、主线文件位置、协作规则与交接入口。

## root path
- project_root:

## mainline files
- brief: `00-brief/brief.md`
- status: `01-status/status.json`
- next_step: `01-status/next-step.md`
- decision_log: `02-decisions/decision-log.md`

## folder guide
- `00-brief/`：项目简报与主线背景
- `01-status/`：当前状态、下一步、主线进度
- `02-decisions/`：关键决策、范围变化、路径调整
- `03-input/`：输入材料、外部资料、历史文件
- `04-working/`：工作草稿、分析过程、临时产物
- `05-review/`：待会审、待 review 版本
- `06-final/`：最终交付版本

## collaboration rules
- 正式推进优先以 `00-brief/`、`01-status/`、`02-decisions/` 为准
- 接手前先读主线文件
- 不要把 `04-working/` 草稿直接当最终结论
- 如发现文件不在共享根目录主线下，应标记为未挂主线并尽快迁回

## handoff entry
接手 agent 进入项目前，至少先读取：
- `00-brief/brief.md`
- `01-status/status.json`
- `01-status/next-step.md`
- 必要时读取 `02-decisions/decision-log.md`
