#!/bin/bash

# Script pour lister tous les jeux présents dans la borne d'arcade

# Vérifier si le dossier projet existe
if [ ! -d "projet" ]; then
    echo "Erreur: Le dossier 'projet' n'existe pas."
    exit 1
fi

# Parcourir tous les dossiers dans projet et afficher uniquement les noms
for jeu in projet/*/; do
    if [ -d "$jeu" ]; then
        basename "$jeu"
    fi
done
