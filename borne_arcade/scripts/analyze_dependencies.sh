#!/bin/bash
# Script d'analyse des dépendances - Wrapper simple

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BORNE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

export BORNE_ROOT

echo "Analyse des dépendances du projet borne_arcade..."
python3 "$SCRIPT_DIR/generate_global_deps.py"
