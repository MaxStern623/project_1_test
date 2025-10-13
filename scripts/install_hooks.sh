#!/usr/bin/env bash
# Installs git hooks to run the pre-push checks locally.
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$ROOT_DIR/.git/hooks"

if [ ! -d "$HOOKS_DIR" ]; then
  echo "No .git/hooks directory found. Are you in a git repo?"
  exit 1
fi

cat > "$HOOKS_DIR/pre-push" <<'HOOK'
#!/usr/bin/env bash
# Run local pre-push checks
"$(dirname "$0")/../scripts/pre_push_check.sh"
HOOK

chmod +x "$HOOKS_DIR/pre-push"
echo "Installed pre-push hook. It will run scripts/pre_push_check.sh before pushing."
