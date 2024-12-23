#!/bin/bash

# CSS Generator Script: Generates CSS for 8 bars with height variations

CSS_FILE="$HOME/.config/waybar/generated_bars.css"
COLORS=("#edff0f" "#6717fe" "#ff0fe7" "#17ffe2" "#edff0f" "#6717fe" "#ff0fe7" "#17ffe2")

# Create or overwrite the CSS file
echo "/* Generated CSS for Waybar bars */" > $CSS_FILE

for i in {1..8}; do
    BAR_ID="custom-bar$i"
    COLOR=${COLORS[$(( (i - 1) % ${#COLORS[@]} ))]}

    # Base bar style
    echo "#$BAR_ID {" >> $CSS_FILE
    echo "    background-color: $COLOR;" >> $CSS_FILE
    echo "    margin: 0 1px; /* Small horizontal spacing */" >> $CSS_FILE
    echo "    padding: 0; /* Reset padding */" >> $CSS_FILE
    echo "    color: transparent; /* Invisible text */" >> $CSS_FILE
    echo "    font-size: 0; /* Invisible text */" >> $CSS_FILE
    echo "}" >> $CSS_FILE

    # Height variations (size-0 to size-20)
    for size in {0..20}; do
        BOTTOM=12
        TOP=$((33 - size))
        echo "#$BAR_ID.size-$size {" >> $CSS_FILE
        echo "    margin-top: ${TOP}px;" >> $CSS_FILE
        echo "    margin-bottom: ${BOTTOM}px;" >> $CSS_FILE
        echo "    padding-right: 3px;" >> $CSS_FILE
        echo "    padding-left: 3px;" >> $CSS_FILE
        echo "}" >> $CSS_FILE
    done

done

# Print completion message
echo "Generated CSS file: $CSS_FILE"
