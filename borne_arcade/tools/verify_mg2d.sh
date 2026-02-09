#!/bin/bash
# Vérification de la bibliothèque MG2D.jar

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/detect_environment.sh" --silent

MG2D_JAR="/home/pi/git/MG2D.jar"

echo "Vérification de MG2D.jar..."

if [ ! -f "$MG2D_JAR" ]; then
    echo "ERREUR: MG2D.jar non trouvé dans /home/pi/git/"
    echo "Veuillez placer MG2D.jar dans ce répertoire avant de continuer."
    exit 1
fi

# Vérification que le fichier est un JAR valide
if ! file "$MG2D_JAR" | grep -q "Java archive"; then
    echo "ERREUR: MG2D.jar n'est pas un fichier JAR valide"
    exit 1
fi

# Vérification de la présence de la classe principale
if ! jar tf "$MG2D_JAR" | grep -q "ApplicationMG2D.class"; then
    echo "ERREUR: MG2D.jar ne contient pas la classe principale ApplicationMG2D"
    exit 1
fi

# Vérification des permissions
if [ ! -r "$MG2D_JAR" ]; then
    echo "ERREUR: MG2D.jar n'est pas lisible"
    exit 1
fi

jar_size=$(ls -lh "$MG2D_JAR" | awk '{print $5}')
echo "MG2D.jar vérifié avec succès ($jar_size)"
echo "MG2D: OK"
