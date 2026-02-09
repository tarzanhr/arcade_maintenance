#!/bin/bash
source "$(dirname "$0")/common.sh"

cd "$BORNE_ROOT/projet/PianoTile"
"$BORNE_ROOT/tools/python_wrapper.sh" app/game.py
