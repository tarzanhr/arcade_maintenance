#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "[0/3] Initializing submodules..."
git -C "$SCRIPT_DIR" submodule update --init --recursive

echo "[1/3] Creating MG2D.jar..."
if [ ! -f "$SCRIPT_DIR/MG2D.jar" ]; then
    bash "$SCRIPT_DIR/create_mg2d_jar.sh"
else
    echo "  MG2D.jar already exists, skipping"
fi

echo "[2/3] Installing system dependencies..."
if [ -f "$SCRIPT_DIR/borne_arcade/tools/install_dependencies.sh" ]; then
    cd "$SCRIPT_DIR/borne_arcade"
    ./tools/install_dependencies.sh
    cd "$SCRIPT_DIR"
else
    echo "  install_dependencies.sh not found, skipping"
fi

echo "[3/3] Installing arcade cabinet..."
bash "$SCRIPT_DIR/borne_arcade/install.sh"
