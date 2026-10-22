#!/usr/bin/env bash
# Initializes a clean ./.builder-os/ state subfolder inside any target project directory.
# Usage: bash /path/to/BUILDER-OS/scripts/init-project-subfolder.sh [target-project-dir]
set -euo pipefail

BUILDER_OS_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="${1:-$(pwd)}"

mkdir -p "$TARGET_DIR/.builder-os"

for f in feature_list.json claude-progress.md init.sh; do
  if [ ! -f "$TARGET_DIR/.builder-os/$f" ]; then
    cp "$BUILDER_OS_ROOT/$f" "$TARGET_DIR/.builder-os/$f"
  fi
done
chmod +x "$TARGET_DIR/.builder-os/init.sh"

for tpl in pitch prfaq design-note build-log launch-checklist; do
  if [ ! -f "$TARGET_DIR/.builder-os/${tpl}.md" ]; then
    cp "$BUILDER_OS_ROOT/os/artifacts/${tpl}-template.md" "$TARGET_DIR/.builder-os/${tpl}.md"
  fi
done

# Crash-resilient scratchpad for the Socratic grill session. Created empty so
# the path always exists and the agent never has to invent one.
if [ ! -f "$TARGET_DIR/.builder-os/grill-notes.md" ]; then
  printf '# Grill Notes\n\nScratchpad for the Socratic interview. Appended after every answer so\nno brainstorming is lost if the context window fills up.\n\n' \
    > "$TARGET_DIR/.builder-os/grill-notes.md"
fi

python3 "$BUILDER_OS_ROOT/scripts/tag_project.py" "$TARGET_DIR/.builder-os" >/dev/null 2>&1 || true

# Initialize git and pre-commit evidence + secret gate if not already present
if [ ! -d "$TARGET_DIR/.git" ]; then
  git -C "$TARGET_DIR" init -q
fi

mkdir -p "$TARGET_DIR/.git/hooks"
# The OS root is resolved at copy time so the hook stays correct even if the
# BUILDER-OS folder is later moved (re-run this script to refresh it).
# The heredoc is intentionally UNQUOTED so $BUILDER_OS_ROOT expands now; every
# other dollar sign below is escaped so the hook's own runtime variables are
# written out literally.
cat << HOOK > "$TARGET_DIR/.git/hooks/pre-commit"
#!/usr/bin/env bash
set -euo pipefail
BUILDER_OS_ROOT="$BUILDER_OS_ROOT"
if [ -f "\$BUILDER_OS_ROOT/scripts/secret-scan.sh" ]; then
  bash "\$BUILDER_OS_ROOT/scripts/secret-scan.sh" .
fi
FEATURE_FILE=".builder-os/feature_list.json"
if [ -f "\$FEATURE_FILE" ]; then
  BLOCK_REASON=\$(node -e "
    const { execSync } = require('child_process');
    const fs = require('fs');
    const stripBom = s => s.replace(/^\uFEFF/, '');
    let prevData = { features: [] };
    try {
      prevData = JSON.parse(stripBom(execSync('git show HEAD:.builder-os/feature_list.json', { encoding: 'utf8', stdio: ['pipe', 'pipe', 'ignore'] })));
    } catch {}
    const data = JSON.parse(stripBom(fs.readFileSync('.builder-os/feature_list.json', 'utf8')));
    for (const f of (data.features || [])) {
      const prev = (prevData.features || []).find(p => p.id === f.id);
      if (f.status === 'passing' && prev?.status !== 'passing' && (!f.evidence || f.evidence.length === 0)) {
        process.stdout.write('Feature ' + f.id + ' is transitioning to passing with no evidence recorded.');
        break;
      }
    }
  " 2>/dev/null || echo "")
  if [ -n "\$BLOCK_REASON" ]; then
    echo "COMMIT BLOCKED: \$BLOCK_REASON"
    exit 1
  fi
fi
HOOK
chmod +x "$TARGET_DIR/.git/hooks/pre-commit"
git -C "$TARGET_DIR" config core.hooksPath .git/hooks

# .builder-os/ MUST stay tracked: the pre-commit gate reads the previous
# committed state via `git show HEAD:.builder-os/feature_list.json`.
if [ -f "$TARGET_DIR/.gitignore" ] && grep -q "^\.builder-os" "$TARGET_DIR/.gitignore"; then
  echo "[.builder-os] WARNING: .builder-os/ is gitignored; the pre-commit evidence gate needs it tracked."
fi

echo "[.builder-os] Initialized clean state subfolder in $TARGET_DIR/.builder-os/"
