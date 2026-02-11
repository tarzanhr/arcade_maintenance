#!/bin/bash
source "$(dirname "$0")/common.sh"

setxkbmap borne

cd "$BORNE_ROOT"

echo "Lancement menu..."

./scripts/liste_jeux.sh > temp

# Vérifier si la liste des jeux a changé
if [ ! -f "noms_jeux.txt" ] || ! diff -q temp noms_jeux.txt > /dev/null; then
    echo "La liste des jeux a changé, lancement de la compilation..."
    ./compilation.sh
    mv temp noms_jeux.txt
else
    echo "La liste des jeux n'a pas changé, pas de compilation nécessaire."
    rm temp
fi

java -cp "$JAVA_CP" Main

# Extinction de la borne après l'avoir quitté
#for i in {30..1}
#do
#    echo Extinction de la borne dans $i secondes
#    sleep 1
#done

#sudo halt
