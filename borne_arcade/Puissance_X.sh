#!/bin/bash
source "$(dirname "$0")/common.sh"

xdotool mousemove 1280 1024
cd "$BORNE_ROOT/projet/Puissance_X"
java -cp ".:../..:$MG2D_PATH" -Dsun.java2d.pmoffscreen=false Main
