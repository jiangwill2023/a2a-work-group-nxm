# ack check sop

## purpose
按 `task_id` 精准检查目标 session 是否已经回 `ACK` / `BLOCKED`。

## standard steps
1. 确认目标 `session key`
2. 调用：
   - `openclaw gateway call sessions.get --json --params '{"key":"<session_key>"}'`
3. 在返回内容中搜索指定 `task_id`
4. 判断后续 assistant 回复是否为：
   - `ACK`
   - `BLOCKED`
   - 未找到
5. 输出结构化回执：
   - `task_id`
   - `session_key`
   - `status`
   - `evidence seq`
   - `evidence snippet`

## result states
- `ACKED`
- `BLOCKED`
- `RECEIVED`（有后续外部证据确认对方已收到，但 session 侧尚未提取到明确 ACK/BLOCKED）
- `TASK_ID_NOT_FOUND`
- `SESSION_READ_FAILED`

## interpretation rule
- `timeout` 只表示当前窗口内没拿到即时回执
- 如后续人工/外部证据确认已收到，应把状态更新为 `RECEIVED`

## reminder
- 不要只看 `sessions.send -> status: started`
- 真正闭环必须以 `sessions.get` 证据为准
