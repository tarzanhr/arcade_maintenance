#!/bin/bash
# Mise à jour de la borne

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Mise à jour ==="

# Git pull pour récupérer les dernières modifications
echo "Pull depuis Git..."
cd ..
git pull origin main

# Mise à jour des sous-modules
echo "Mise à jour des sous-modules..."
git submodule update --init --recursive

cd borne_arcade

if [ -f ./clean.sh ]; then
    echo "Nettoyage..."
    ./clean.sh
fi

if [ -f ./compilation.sh ]; then
    echo "Compilation..."
    ./compilation.sh
fi

if [ -f ./scripts/safe_update.sh ]; then
    echo "Mise à jour des paquets..."
    ./scripts/safe_update.sh
fi

echo "Mise à jour terminée"
