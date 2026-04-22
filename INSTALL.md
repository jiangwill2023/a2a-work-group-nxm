# A2A work group nxm - 安装说明

## 安装方式

### 方式 1：直接复制到 OpenClaw skills 目录
```bash
cp -r a2a-work-group-nxm ~/.openclaw/skills/
```

### 方式 2：通过 OpenClaw CLI 安装（未来支持）
```bash
openclaw skills install a2a-work-group-nxm
```

## 安装后验证
```bash
python3 ~/.openclaw/skills/a2a-work-group-nxm/scripts/workgroup_cli.py \
  --project-name "test" \
  --shortname "test" \
  --requester "will" \
  --task-type "research" \
  --session-key "agent:mr-library:discord:channel:1480155817952153651" \
  --task-id "test-20260421-01" \
  --request-summary "test installation"
```

## 依赖
- Python >= 3.9
- OpenClaw >= 2026.4.15
- 共享根目录 `/Volumes/Local Drawer/SharedProjects/` 已存在

## 配置
- `config/team-role-map.json`：团队角色映射
- `config/template-map.json`：项目模板选择
- `skill.json`：skill 元数据

## 权限要求
- `sessions.send`
- `sessions.get`
- `sessions.list`
- `exec`
- `read`
- `write`
