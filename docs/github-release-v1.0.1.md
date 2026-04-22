# Release v1.0.1 - Public-Ready Standardization

## Summary

This release turns `a2a-work-group-nxm` from an internal working package into a public-ready OpenClaw skill.

## What's changed

### Public-ready cleanup
- Replaced real team member names with role placeholders
- Replaced machine-specific paths with configurable placeholders
- Removed internal-only Chinese documentation from the public bundle
- Removed direct references to private sender IDs, session keys, and channel IDs

### Config improvements
- Added `config/team-role-map.example.json`
- Added `config/settings.example.json`
- Updated scripts to read `shared_root` from config instead of hardcoded paths

### Documentation improvements
- Updated `README.md` to public-facing style
- Updated `SKILL.md` and `INSTALL.md`
- Added `docs/public-release-checklist.md`

## Why this matters

The skill is now safer to share publicly and easier for third parties to adopt without inheriting private environment assumptions.

## Repository

https://github.com/jiangwill2023/a2a-work-group-nxm
