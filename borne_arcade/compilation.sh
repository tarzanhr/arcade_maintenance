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
javac $JAVAC_FLAGS -cp "$JAVA_CP" *.java

cd projet

for i in *
do
    cd $i
    echo "Compilation jeu $i"
    javac $JAVAC_FLAGS -cp "$JAVA_CP:../.." *.java 2>/dev/null || true
    cd ..
done

cd ..
