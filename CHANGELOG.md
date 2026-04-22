# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2026-04-22

### Changed
- Public-ready standardization
- Replaced real team member names with role placeholders
- Replaced machine-specific paths with configurable placeholders
- Added example config files (`team-role-map.example.json`, `settings.example.json`)
- Removed internal Chinese documentation from public bundle
- Updated README, SKILL.md, INSTALL.md to public-facing style
- Updated scripts to read shared_root from config instead of hardcoding
- Added public release checklist

## [1.0.0] - 2026-04-21

### Added
- Initial release of A2A Work Group NXM skill
- Unified CLI entry (`workgroup_cli.py`)
- Automatic task routing based on task type
- Project initialization with standardized templates
- A2A dispatch with ACK/BLOCKED/timeout tracking
- Multi-target dispatch support
- Retry mechanism for pending tasks
- Project health check
- Checkpoint writing for long tasks
- System deployment sync
- Team role map configuration
- Template selection (standard/minimal/full)
- Complete documentation suite
- MIT License

### Features
- Support for 5 PM roles + 2 assistant roles + finance support
- Project ID format: `p-YYYYMMDD-shortname`
- Shared root directory with space-safe path handling
- Status governance with 6 states: planning, ready, in_progress, review, blocked, done
- Decision log and progress log templates
- Handoff checklist
- Cross-session communication with proper tool permissions

### Documentation
- SKILL.md - Skill design and architecture
- README.md - User-facing documentation
- INSTALL.md - Installation guide
- CONTRIBUTING.md - Contribution guidelines
- CHANGELOG.md - This file
- docs/ - Additional SOPs and templates

## [0.1.0] - 2026-04-18

### Added
- Initial design draft
- Project template structure
- A2A dispatch templates
- ACK check SOP
- Team role map
- Shared projects bootstrap

[1.0.1]: https://github.com/OWNER/a2a-work-group-nxm/releases/tag/v1.0.1
[1.0.0]: https://github.com/OWNER/a2a-work-group-nxm/releases/tag/v1.0.0
[0.1.0]: https://github.com/OWNER/a2a-work-group-nxm/releases/tag/v0.1.0
