# A2A Work Group NxM - Multi-Agent Collaboration Skill for OpenClaw

## 🎯 What is it?

A production-ready skill for OpenClaw that enables **N×M multi-agent collaboration** with structured project management, automatic routing, ACK tracking, and checkpoint synchronization.

## ✨ Key Features

- **Project Initialization**: Standardized project structure with templates
- **Smart Routing**: Automatic task dispatch based on role mapping
- **ACK Tracking**: Built-in acknowledgment and status monitoring
- **Checkpoint Management**: Automated progress tracking and handoff
- **Cross-Session Communication**: Reliable agent-to-agent messaging
- **Configurable**: Easy to adapt to your team structure

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/jiangwill2023/a2a-work-group-nxm.git
cd a2a-work-group-nxm

# Configure
cp config/settings.example.json config/settings.json
cp config/team-role-map.example.json config/team-role-map.json
# Edit config files with your team setup

# Use
python scripts/workgroup_cli.py create --project-name "my-project" --brief "Project description"
```

## 📦 What's Included

- **11 Core Scripts**: Project lifecycle management
- **6 Templates**: Ready-to-use project structures
- **9 Documentation Files**: Complete guides and specs
- **Configuration System**: Flexible role and template mapping

## 🎓 Use Cases

- Multi-agent software development teams
- Research collaboration workflows
- Content production pipelines
- Any scenario requiring structured agent coordination

## 📖 Documentation

- [Installation Guide](INSTALL.md)
- [Skill Documentation](SKILL.md)
- [Design Document](docs/A2A_work_group_nxm_skill_design_v1_2026-04-21.md)
- [Collaboration Spec](docs/team_collaboration_spec_v2_draft_2026-04-18.md)

## 🔗 Links

- **GitHub**: https://github.com/jiangwill2023/a2a-work-group-nxm
- **License**: MIT
- **Version**: 1.0.1

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

Built for the OpenClaw ecosystem 🐾
