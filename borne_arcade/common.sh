#!/bin/bash
# Configuration commune pour tous les scripts

COMMON_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$COMMON_DIR/config/paths.conf"
