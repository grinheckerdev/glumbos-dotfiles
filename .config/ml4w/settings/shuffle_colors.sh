#!/bin/bash

# Define the colors
colors=("#6817fd" "#edfd10" "#fe0eea" "#18fcdf")

# Determine the current index based on time
current_index=$(($(date +%s) % ${#colors[@]}))


# Output the :3 with the current color
echo "<span foreground='${colors[$current_index]}'>:3</span>"
