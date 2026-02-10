#!/bin/bash
source "$(dirname "$0")/common.sh"

cd "$BORNE_ROOT/projet/ball-blast"
"$BORNE_ROOT/tools/python_wrapper.sh" ./src
