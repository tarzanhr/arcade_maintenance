#!/bin/bash
# Configuration de l'autostart

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BORNE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
AUTOSTART_DIR="$HOME/.config/autostart"

mkdir -p "$AUTOSTART_DIR"

cat > "$AUTOSTART_DIR/borne.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=Borne Arcade
Exec=/usr/bin/lxterminal -e $BORNE_ROOT/lancerBorne.sh
Terminal=true
X-KeepTerminal=false
EOF

echo "Autostart: OK"
