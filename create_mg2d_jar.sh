#!/bin/bash
# Script simple pour créer MG2D.jar une seule fois

set -e

echo "Création de MG2D.jar..."

# Vérification Java
if ! command -v javac &> /dev/null; then
    echo "ERREUR: javac non trouvé. Installez Java JDK."
    exit 1
fi

# Clone temporaire
echo "Clonage de MG2D..."
if [ -d "temp_mg2d" ]; then
    rm -rf temp_mg2d
fi
git clone https://github.com/synave/MG2D.git temp_mg2d

# Vérification de la structure
echo "Vérification de la structure..."
cd temp_mg2d
if [ -d "MG2D" ]; then
    echo "Sources trouvées dans temp_mg2d/MG2D/"
    SOURCE_DIR="MG2D"
else
    echo "Sources trouvées dans temp_mg2d/"
    SOURCE_DIR="."
fi

# Compilation
echo "Compilation..."
mkdir -p ../build/classes
javac -d ../build/classes -encoding UTF-8 $SOURCE_DIR/*.java 2>/dev/null || echo "Pas de fichiers .java à la racine"
javac -d ../build/classes -encoding UTF-8 $SOURCE_DIR/geometrie/*.java 2>/dev/null || echo "Pas de fichiers dans geometrie/"
javac -d ../build/classes -encoding UTF-8 $SOURCE_DIR/audio/*.java 2>/dev/null || echo "Pas de fichiers dans audio/"

# Création JAR
echo "Création du JAR..."
cd ../build/classes
echo "Contenu du dossier build/classes:"
ls -la

echo "Recherche des fichiers .class:"
find . -name "*.class" | head -5

jar cfe ../MG2D.jar ApplicationMG2D . 2>/dev/null && echo "JAR créé avec ApplicationMG2D" || {
    jar cfe ../MG2D.jar MG2D.ApplicationMG2D . 2>/dev/null && echo "JAR créé avec MG2D.ApplicationMG2D" || {
        echo "Recherche de la classe principale..."
        MAIN_CLASS=$(find . -name "*ApplicationMG2D*" -o -name "*MG2D*" | head -1 | sed 's|\.class||' | sed 's|^\./||')
        echo "Classe principale trouvée: $MAIN_CLASS"
        if [ -n "$MAIN_CLASS" ]; then
            jar cfe ../MG2D.jar "$MAIN_CLASS" . && echo "JAR créé avec $MAIN_CLASS"
        else
            echo "Création JAR sans classe principale..."
            jar cf ../MG2D.jar . && echo "JAR créé sans classe principale"
        fi
    }
}
cd ../..

# Nettoyage
mv build/MG2D.jar ./MG2D.jar
rm -rf temp_mg2d build/

# Vérification
if [ -f MG2D.jar ]; then
    size=$(ls -lh MG2D.jar | awk '{print $5}')
    echo "✅ MG2D.jar créé avec succès ($size)"
    echo "Place-le dans /home/pi/git/ si nécessaire"
else
    echo "❌ Échec de la création du JAR"
    exit 1
fi
