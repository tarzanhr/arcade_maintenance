#!/bin/bash
# Wrapper Python multi-version

PYTHON_VERSIONS=("python3.12" "python3.11" "python3.10" "python3.9" "python3.7" "python3.5" "python3")

for py_cmd in "${PYTHON_VERSIONS[@]}"; do
    if command -v "$py_cmd" &> /dev/null; then
        exec "$py_cmd" "$@"
    fi
done

echo "Erreur: Python 3 introuvable" >&2
exit 1
