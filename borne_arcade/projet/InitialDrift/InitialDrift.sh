#!/bin/bash
xdotool mousemove 1280 1024
cd "$BORNE_ROOT/projet/InitialDrift"
touch highscore
java -cp ".:../..:$BORNE_ROOT/bin:$MG2D_JAR" Main
