#!/bin/bash

# Path to the widget script
WIDGET_SCRIPT="~/.config/hypr/custom_glumbocoin_widget.py"

# Set the DISPLAY variable (adjust if necessary)
export DISPLAY=:0

# Debug log
LOG_FILE="/tmp/toggle_glumbocoin.log"

echo "$(date): Script started" >> "$LOG_FILE"

# Check if the widget is running
if pgrep -f "$WIDGET_SCRIPT" > /dev/null; then
    echo "$(date): Killing widget..." >> "$LOG_FILE"
    pkill -9 -f "python3.*custom_glumbocoin_widget.py" && echo "$(date): Widget killed" >> "$LOG_FILE"
else
    echo "$(date): Starting widget..." >> "$LOG_FILE"
    python3 "$WIDGET_SCRIPT" &>> "$LOG_FILE" &
    echo "$(date): Widget launched" >> "$LOG_FILE"
fi
