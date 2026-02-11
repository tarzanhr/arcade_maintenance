#!/bin/bash
source "$(dirname "$0")/common.sh"

xdotool mousemove 1280 1024
cd "$BORNE_ROOT/projet/Puissance_X"
java -cp ".:../..:$BORNE_ROOT/bin:$MG2D_JAR" -Dsun.java2d.pmoffscreen=false Main
