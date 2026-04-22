# Contributing to A2A Work Group NXM

Thank you for your interest in contributing! This project is part of the OpenClaw ecosystem for multi-agent collaboration.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/a2a-work-group-nxm.git`
3. Install to your OpenClaw skills directory for testing

## Development Setup

```bash
# Install locally for testing
cp -r a2a-work-group-nxm ~/.openclaw/skills/

# Test the CLI
python3 ~/.openclaw/skills/a2a-work-group-nxm/scripts/workgroup_cli.py --help
```

## Making Changes

### Code Style
- Python scripts should include shebang: `#!/usr/bin/env python3`
- Use type hints where practical
- Include docstrings for functions
- Handle paths with spaces safely (quoted paths)

### Testing
- Test with actual OpenClaw sessions when possible
- Verify path handling with spaces: `/Volumes/Local Drawer/SharedProjects/`
- Check ACK/BLOCKED/timeout states

### Documentation
- Update README.md if adding features
- Update CHANGELOG.md with version bumps
- Add to docs/ for SOPs or detailed guides

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes with clear commit messages
3. Update documentation as needed
4. Test thoroughly
5. Submit PR with description of changes

## Areas for Contribution

### High Priority
- [ ] Multi-project concurrent governance
- [ ] Automatic project health monitoring
- [ ] Exception project auto-flagging
- [ ] Better template customization

### Nice to Have
- [ ] Web UI for project status dashboard
- [ ] Integration with external calendars
- [ ] Slack/Teams adapter
- [ ] More template types

## Questions?

Open an issue or reach out to the OpenClaw community.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
