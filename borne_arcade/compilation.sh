#!/bin/bash
source "$(dirname "$0")/common.sh"
source "$SCRIPT_DIR/tools/detect_environment.sh" --silent

JAVA_VERSION=$(java -version 2>&1 | head -1 | cut -d'"' -f2 | cut -d'.' -f1)
if [ "$JAVA_VERSION" = "1" ]; then
    JAVA_VERSION=$(java -version 2>&1 | head -1 | cut -d'"' -f2 | cut -d'.' -f2)
fi

if [ "$JAVA_VERSION" -ge 17 ] 2>/dev/null; then
    JAVAC_FLAGS=""
else
    JAVAC_FLAGS="-source 8 -target 8"
fi

echo "Compilation menu (Java $JAVA_VERSION)"
mkdir -p bin
javac $JAVAC_FLAGS -d bin -cp "$JAVA_CP" src/*.java

cd projet

for i in *
do
    cd $i
    echo "Compilation jeu $i"
    if ls *.java 1> /dev/null 2>&1; then
        javac $JAVAC_FLAGS -cp "$JAVA_CP:../../bin:../.." *.java
    else
        echo "  Pas de fichiers .java à compiler"
    fi
    cd ..
done

cd ..

./scripts/liste_jeux.sh > data/noms_jeux.txt

# Donner les permissions d'exécution aux scripts de lancement
echo -e "\nDonner les permissions d'exécution aux scripts de lancement..."
./scripts/set_executable.sh
