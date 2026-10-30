# Code Review Checklist

Use this for every pull request. Tick what applies and comment on what does not.

## Purpose and scope
- [ ] 1. The PR does one thing, and its title and description explain why, not only what.
- [ ] 2. It links an issue, and the change actually satisfies that issue.
- [ ] 3. The PR is small enough to review properly (roughly under 400 changed lines). Large changes are split.

## Correctness and reliability
- [ ] 4. The logic is correct, including edge cases and failure paths (missing arguments, failed commands, empty input).
- [ ] 5. Errors are handled and visible: strict mode or exit checks, meaningful exit codes, clear error messages.
- [ ] 6. The change can be rolled back safely and does not break existing behaviour or configuration.

## Security
- [ ] 7. No secrets, tokens, keys, or passwords appear in the diff, logs, or commit history.
- [ ] 8. Inputs are validated and quoted, permissions are least-privilege, and new dependencies, base images, or actions are from trusted sources and pinned.

## Quality and maintainability
- [ ] 9. Names are descriptive and consistent, and the code is readable without asking the author. Comments explain why, not what.
- [ ] 10. Linters pass (ShellCheck, hadolint) and CI is green, with no ignored warnings left unexplained.

## Verification and documentation
- [ ] 11. Testing is shown: tests added or testing notes that a reviewer could repeat.
- [ ] 12. README, comments, and runbooks are updated when behaviour or configuration changes.
