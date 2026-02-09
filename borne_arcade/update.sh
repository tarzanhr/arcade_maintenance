#!/bin/bash
# Mise à jour de la borne

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Mise à jour ==="

echo "MG2D..."
./tools/setup_mg2d.sh

if [ -f ./clean.sh ]; then
    echo "Nettoyage..."
    ./clean.sh
fi

if [ -f ./compilation.sh ]; then
    echo "Compilation..."
    ./compilation.sh
fi

echo "Mise à jour terminée"
