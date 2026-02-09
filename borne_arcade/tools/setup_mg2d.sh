#!/bin/bash
# Setup de la bibliothèque MG2D

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/detect_environment.sh" --silent

MG2D_PATH="${MG2D_PATH:-/home/pi/git/MG2D}"
MG2D_REPO="https://github.com/synave/MG2D.git"

if [ -d "$MG2D_PATH" ]; then
    echo "MG2D: mise à jour..."
    cd "$MG2D_PATH"
    git pull -q
else
    echo "MG2D: clonage..."
    git clone -q "$MG2D_REPO" "$MG2D_PATH"
fi

echo "MG2D: OK"
