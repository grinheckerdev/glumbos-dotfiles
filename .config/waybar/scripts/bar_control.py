#!/usr/bin/env python3

import os
import struct
import subprocess
import tempfile
import json
import sys

BAR_ID = int(sys.argv[1])  # Bar ID to manage (1-based index)
BARS_TOTAL = 8  # Total number of bars
STATE_FILE = f"/tmp/bar{BAR_ID}_state.txt"

# Initialize the state file if it doesn't exist
if not os.path.exists(STATE_FILE):
    with open(STATE_FILE, "w") as f:
        f.write("0")

# Define Cava configuration
CAVA_CONFIG = "/tmp/cava_config"
with open(CAVA_CONFIG, "w") as f:
    f.write(
        f"""
        [general]
        bars = {BARS_TOTAL}
        [output]
        method = raw
        raw_target = /dev/stdout
        bit_format = 8bit
        """
    )

# Start Cava as a subprocess
cava_process = subprocess.Popen(
    ["cava", "-p", CAVA_CONFIG],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

try:
    while True:
        # Read a single chunk corresponding to all bars
        data = cava_process.stdout.read(BARS_TOTAL)
        if not data or len(data) < BARS_TOTAL:
            break

        # Extract the level for the current bar
        LEVEL = data[BAR_ID - 1]

        # Cap LEVEL at 255
        if LEVEL > 255:
            LEVEL = 255
        elif LEVEL < 0:
            LEVEL = 0

        # Scale the value to 0-20
        NEW_SIZE = LEVEL * 20 // 255

        # Update the state file with the new size
        with open(STATE_FILE, "w") as f:
            f.write(str(NEW_SIZE))

        # Output the JSON for Waybar
        output = {"text": "bar", "class": f"size-{NEW_SIZE}"}
        print(json.dumps(output), flush=True)

except KeyboardInterrupt:
    pass
finally:
    # Clean up the Cava process on exit
    cava_process.terminate()
    cava_process.wait()
