#!/bin/bash
# Configuration système

set -e

if command -v xset &> /dev/null; then
    xset s off 2>/dev/null || true
    xset -dpms 2>/dev/null || true
    xset s noblank 2>/dev/null || true
fi

if ! dpkg -l | grep -q "^ii  unclutter "; then
    sudo apt-get install -y -qq unclutter 2>/dev/null || true
fi
