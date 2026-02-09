#!/bin/bash
source "$(dirname "$0")/common.sh"

xdotool mousemove 1280 1024
cd "$BORNE_ROOT/projet/Kowasu_Renga"
touch highscore
java -cp ".:../..:$(dirname "$MG2D_PATH")" Kowasu_Renga
