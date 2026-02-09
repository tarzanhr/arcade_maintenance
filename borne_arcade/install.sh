#!/bin/bash
# Installation de la borne d'arcade

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Installation Borne d'Arcade ==="

if ! grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null && [ -z "$FORCE_INSTALL" ]; then
    echo "Attention: pas un Raspberry Pi"
    read -p "Continuer? (o/N) " -r
    if [[ ! $REPLY =~ ^[OoYy]$ ]]; then
        exit 1
    fi
fi

source ./tools/detect_environment.sh

echo "[1/7] Installation dépendances..."
./tools/install_dependencies.sh

echo "[2/7] Setup MG2D..."
./tools/setup_mg2d.sh

echo "[3/7] Installation layout clavier..."
./tools/install_keyboard_layout.sh

echo "[4/7] Compilation..."
if [ -f ./compilation.sh ]; then
    ./compilation.sh
else
    echo "compilation.sh non trouvé, ignoré"
fi

echo "[5/7] Configuration autostart..."
./tools/setup_autostart.sh

echo "[6/7] Configuration système..."
./tools/configure_system.sh

echo "[7/7] Installation git hooks..."
if [ -d .git ]; then
    cp tools/git-hooks/* .git/hooks/ 2>/dev/null || echo "Pas de git hooks"
    chmod +x .git/hooks/* 2>/dev/null || true
fi

echo ""
echo "Installation terminée!"
echo "Redémarrez pour lancer automatiquement la borne"
