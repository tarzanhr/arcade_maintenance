#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "[1/2] Creating MG2D.jar..."
if [ ! -f "$SCRIPT_DIR/MG2D.jar" ]; then
    bash "$SCRIPT_DIR/create_mg2d_jar.sh"
else
    echo "  MG2D.jar already exists, skipping"
fi

echo "[2/2] Installing arcade cabinet..."
bash "$SCRIPT_DIR/borne_arcade/install.sh"
