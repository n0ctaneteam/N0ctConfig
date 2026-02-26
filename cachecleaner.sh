#!/usr/bin/env bash

# Directory to watch (change this!)
WATCH_DIR="$HOME/.config/N0ctConfig"

POLL_INTERVAL=0.2

echo "[cache-pruner] Watching: $WATCH_DIR"

while true; do
    find "$WATCH_DIR" -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null
    sleep "$POLL_INTERVAL"
done