#!/bin/bash
# Détection de l'environnement système

set -e

detect_os_version() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        echo "$VERSION_CODENAME"
    else
        echo "unknown"
    fi
}

detect_java_version() {
    if command -v java &> /dev/null; then
        local java_version=$(java -version 2>&1 | head -1 | cut -d'"' -f2)
        local major_version=$(echo "$java_version" | cut -d'.' -f1)
        if [ "$major_version" = "1" ]; then
            major_version=$(echo "$java_version" | cut -d'.' -f2)
        fi
        echo "$major_version"
    else
        echo "none"
    fi
}

detect_python_version() {
    if command -v python3 &> /dev/null; then
        python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2
    else
        echo "none"
    fi
}

detect_architecture() {
    uname -m
}

is_raspberry_pi() {
    if grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then
        echo "yes"
    else
        echo "no"
    fi
}

export BORNE_OS_VERSION=$(detect_os_version)
export BORNE_JAVA_VERSION=$(detect_java_version)
export BORNE_PYTHON_VERSION=$(detect_python_version)
export BORNE_ARCH=$(detect_architecture)
export BORNE_IS_RPI=$(is_raspberry_pi)

if [ "${1:-}" != "--silent" ]; then
    echo "OS: $BORNE_OS_VERSION"
    echo "Arch: $BORNE_ARCH"
    echo "Raspberry Pi: $BORNE_IS_RPI"
    echo "Java: $BORNE_JAVA_VERSION"
    echo "Python: $BORNE_PYTHON_VERSION"
fi

is_modern_os() {
    [ "$BORNE_OS_VERSION" = "bookworm" ] || [ "$BORNE_OS_VERSION" = "bullseye" ]
}

is_legacy_os() {
    [ "$BORNE_OS_VERSION" = "stretch" ] || [ "$BORNE_OS_VERSION" = "jessie" ]
}

get_recommended_java_version() {
    if is_modern_os; then echo "17"; else echo "8"; fi
}

get_recommended_python_version() {
    if is_modern_os; then echo "3.11"; else echo "3.5"; fi
}

export -f is_modern_os
export -f is_legacy_os
export -f get_recommended_java_version
export -f get_recommended_python_version
