#!/bin/bash
# Installation du layout clavier personnalisé

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BORNE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
LAYOUT_FILE="$BORNE_ROOT/borne"
SYSTEM_XKB_DIR="/usr/share/X11/xkb/symbols"

if [ ! -f "$LAYOUT_FILE" ]; then
    echo "Erreur: fichier borne introuvable"
    exit 1
fi

echo "Installation layout clavier..."
sudo cp "$LAYOUT_FILE" "$SYSTEM_XKB_DIR/borne"
sudo dpkg-reconfigure -f noninteractive xkb-data 2>/dev/null || true
echo "Layout clavier: OK"
