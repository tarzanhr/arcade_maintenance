#!/bin/bash
source "$(dirname "$0")/common.sh"

xdotool mousemove 1280 1024
cd "$BORNE_ROOT/projet/JavaSpace"
touch highscore
java -cp ".:../..:$MG2D_PATH" Main
