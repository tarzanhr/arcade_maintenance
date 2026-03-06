#!/bin/bash
source "$(dirname "$0")/common.sh"

setxkbmap borne

cd "$BORNE_ROOT"

STATUS_FILE="/tmp/arcade_status"
echo "Chargement..." > "$STATUS_FILE"

python3.9 "$BORNE_ROOT/tools/splash_screen.py" &
SPLASH_PID=$!

echo "Nettoyage..." > "$STATUS_FILE"
./clean.sh

echo "Compilation..." > "$STATUS_FILE"
./compilation.sh

echo "READY" > "$STATUS_FILE"
wait $SPLASH_PID 2>/dev/null || true
rm -f "$STATUS_FILE"

java -cp "bin:$JAVA_CP" Main

# Extinction de la borne après l'avoir quitté
#for i in {30..1}
#do
#    echo Extinction de la borne dans $i secondes
#    sleep 1
#done

#sudo halt
