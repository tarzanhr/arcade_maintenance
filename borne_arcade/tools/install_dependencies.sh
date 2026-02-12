#!/bin/bash
# Installation des dépendances système

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BORNE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/detect_environment.sh" --silent

if ! sudo -n true 2>/dev/null; then
    sudo -v
fi

sudo apt-get update -qq

sudo apt-get install -y -qq git xdotool xkb-data unclutter curl wget love

if is_modern_os; then
    JAVA_PKG="openjdk-17-jdk"
    PYTHON_PKG="python3"
    PYTHON_PIP="python3-pip"
elif is_legacy_os; then
    JAVA_PKG="openjdk-8-jdk"
    PYTHON_PKG="python3"
    PYTHON_PIP="python3-pip"
else
    JAVA_PKG="default-jdk"
    PYTHON_PKG="python3"
    PYTHON_PIP="python3-pip"
fi

if [ "$BORNE_JAVA_VERSION" = "none" ]; then
    echo "Installation de Java ($JAVA_PKG)..."
    sudo apt-get install -y -qq "$JAVA_PKG"
else
    echo "Java $BORNE_JAVA_VERSION déjà installé"
fi

if [ "$BORNE_PYTHON_VERSION" = "none" ]; then
    echo "Installation de Python..."
    sudo apt-get install -y -qq "$PYTHON_PKG"
else
    echo "Python $BORNE_PYTHON_VERSION déjà installé"
fi

if ! command -v pip3 &> /dev/null; then
    echo "Installation de pip..."
    sudo apt-get install -y -qq "$PYTHON_PIP"
fi

echo "Installation des dépendances Python..."
if [ -f "$BORNE_ROOT/scripts/check_and_install_deps.py" ]; then
    python3 "$BORNE_ROOT/scripts/check_and_install_deps.py"
else
    for req_file in "$BORNE_ROOT"/requirements.txt "$BORNE_ROOT/projet"/*/requirements.txt; do
        if [ -f "$req_file" ]; then
            echo "  Installation depuis $(basename $(dirname $req_file))..."
            pip3 install -q -r "$req_file" --user 2>/dev/null || true
        fi
    done
fi

source "$SCRIPT_DIR/detect_environment.sh" --silent
echo ""
echo "Installation terminée"
echo "Java: $BORNE_JAVA_VERSION"
echo "Python: $BORNE_PYTHON_VERSION"
