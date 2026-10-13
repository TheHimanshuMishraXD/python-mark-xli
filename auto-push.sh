#!/bin/bash

REPO="/home/batman/python code with harry"
cd "$REPO" || exit 1

# Prevent multiple instances from running together
exec 9>/tmp/python-harry-auto-push.lock
if ! flock -n 9; then
    echo "⚠️ Auto-push is already running!"
    exit 1
fi

echo "🚀 Auto-push started..."
echo "Watching: $REPO"
echo "Press Ctrl+C to stop."

while true; do
    inotifywait -r -e close_write,create,delete,move \
        --exclude '(^|/)\.git(/|$)' \
        "$REPO" >/dev/null 2>&1

    sleep 3

    git add -A || {
        echo "❌ git add failed"
        continue
    }

    if ! git diff --cached --quiet; then
        if ! git commit -m "Update Python practice"; then
            echo "❌ Commit failed"
            continue
        fi
    fi

    # Push pending commits, even if the commit happened earlier
    if git push origin main; then
        echo "✅ Push successful!"
    else
        echo "⚠️ Push failed. Checking remote updates..."
        if git fetch origin &&
           git rebase origin/main &&
           git push origin main; then
            echo "✅ Push successful after syncing!"
        else
            echo "❌ Push still failed. Check Git status."
        fi
    fi
done
