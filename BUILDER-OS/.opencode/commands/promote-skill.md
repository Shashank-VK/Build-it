---
description: Promote an inert skill from the library into the active skill set
agent: build
---

Promote the skill named below from the inert library into the active skill set.

**Skill:** $ARGUMENTS

## Steps

1. Resolve the library and active directories:
   - Library: `~/.agents/library/`
   - Active:  `~/.agents/skills/`

2. If `$ARGUMENTS` is empty, list the available library skills and stop:
   ```bash
   ls ~/.agents/library/
   ```
   Also show `~/.agents/library/INDEX.md` if it exists — it lists every stored
   skill with a one-line purpose.

3. Resolve the skill name to a directory. Accept an exact directory name, and
   also accept a case-insensitive or substring match. If exactly one skill
   matches, use it. If several match, list the candidates with their
   descriptions from `INDEX.md` and ask which one — do not guess.

4. Verify the source:
   ```bash
   test -d ~/.agents/library/<name> && test -f ~/.agents/library/<name>/SKILL.md
   ```
   If the skill is not in the library, check whether it is already active in
   `~/.agents/skills/` and report that instead of failing.

5. Move it into the active set:
   ```bash
   mv ~/.agents/library/<name> ~/.agents/skills/<name>
   ```
   Use `mv`, not a copy — the library must not retain a duplicate.

6. Verify it is now discoverable. All harnesses read the shared
   `~/.agents/skills/` path (OpenCode via `~/.config/opencode/skills` and
   Claude Code via `~/.claude/skills` are symlinks to it), so a single move
   activates it everywhere. Confirm the skill directory and its `SKILL.md`
   exist and that the frontmatter parses.

7. Report the promotion: skill name, source repo if known, and the fact that
   it is now active in every harness. Note that the harness may need a
   session restart to pick up the new skill.

8. To demote a skill later, move its directory back to `~/.agents/library/`.
