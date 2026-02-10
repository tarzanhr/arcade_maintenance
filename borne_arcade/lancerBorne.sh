#!/bin/bash
source "$(dirname "$0")/common.sh"

setxkbmap borne

cd "$BORNE_ROOT"

echo "Lancement menu..."

java -cp "$JAVA_CP" Main

# Extinction de la borne après l'avoir quitté
#for i in {30..1}
#do
#    echo Extinction de la borne dans $i secondes
#    sleep 1
#done

#sudo halt
