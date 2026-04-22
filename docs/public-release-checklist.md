# Public Release Checklist

## Identity and Privacy
- [ ] Remove real usernames, channel IDs, session keys, sender IDs
- [ ] Replace real team member names with role placeholders
- [ ] Replace machine-specific paths with configurable placeholders
- [ ] Remove internal-only docs or move them to a private repo

## Documentation
- [ ] Keep public-facing docs in English
- [ ] Move localized/internal docs into `docs/zh/` or private repo
- [ ] Provide example config files instead of private defaults
- [ ] Ensure README uses placeholders only

## Code and Config
- [ ] Avoid hardcoded shared root paths
- [ ] Avoid hardcoded personal role maps
- [ ] Mark local deployment scripts as optional/internal
- [ ] Verify scripts run with example config

## Release
- [ ] Bump version
- [ ] Update CHANGELOG
- [ ] Tag release
- [ ] Create GitHub release notes
