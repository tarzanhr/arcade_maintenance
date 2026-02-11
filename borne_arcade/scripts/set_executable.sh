#!/bin/bash

# Script pour donner les permissions d'exécution uniquement aux fichiers .sh valides

echo "Recherche des fichiers .sh valides dans le dossier projet..."

# Vérifier si le dossier projet existe
if [ ! -d "projet" ]; then
    echo "Erreur: Le dossier 'projet' n'existe pas."
    exit 1
fi

# Compter et rendre exécutables uniquement les fichiers .sh qui correspondent au nom du dossier
count=0
for jeu_dir in projet/*/; do
    if [ -d "$jeu_dir" ]; then
        # Extraire le nom du jeu (nom du dossier)
        nom_jeu=$(basename "$jeu_dir")
        script_path="$jeu_dir$nom_jeu.sh"
        
        # Vérifier si le script existe et a le bon nom
        if [ -f "$script_path" ]; then
            echo "chmod +x $script_path"
            chmod +x "$script_path"
            count=$((count + 1))
        else
            echo "  Script manquant ou incorrect: $script_path"
        fi
    fi
done

echo ""
echo "Terminé ! $count fichier(s) .sh valide(s) rendu(s) exécutable(s)."
