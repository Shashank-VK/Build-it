# Solo AI Product Engineering System v1.0
# Quality, Security, and Reliability System

## Quality Gates per PR

HARD (no override permitted):
- Automated tests must pass (exit code 0)
- Linting must pass (zero errors)

SOFT (human can override with documented reason written into the PR):
- AI style review against locked rubric must pass OR human documents the exception

STAKES TIERING:
- LOW-STAKES: AI-first, cursory human review (UI formatting, simple logic, docs)
- MEDIUM-STAKES: AI-assisted, careful line-by-line human review (business logic, integrations, error handling)
- HIGH-STAKES: AI draft + independent human re-implementation + comparison before merge (financial data, auth, session management, irreversible data operations, cryptography)

## Security Minimum Bar (Launch Checklist items 5-7)

- No secrets hardcoded in the repository (verified by scripts/secret-scan.sh before every launch)
- All external inputs validated and sanitized
- Authentication + authorization tested adversarially: attempt to access a resource without permission and confirm it is blocked

## Reliability Minimum Bar (Launch Checklist items 3-4 and 8)

- Rollback plan tested in staging before first production deploy (not designed — actually executed)
- Error rate alert configured and verified to fire before launch
- Load tested at 2x expected volume before launch

## Pre-Tool Security Guard Behaviors (pre_tool_guard.py)

Guard BLOCKS (fatal error) on:
- rm with recursive/force flags on system paths (/etc, /usr, /var, /home, /root, /sys, /proc)
- curl | sudo bash or curl | python (script injection patterns)
- wget | bash (script injection)
- git push with +main or +master or --force to main/master (force push to protected branches)
- AWS STS credential patterns (ASIA + 16 uppercase alphanumeric characters)
- Unquoted secret patterns in command arguments (password=, api_key=, token= followed by 20+ chars)
