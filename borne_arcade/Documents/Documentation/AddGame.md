# Ajouter un jeu dans la borne d'arcade

Pour ajouter un jeu dans la borne, vous devez suivre les étapes suivantes :

## Étapes obligatoires

1. **Créer le dossier du jeu**
   ```bash
   mkdir projet/<nom du jeu>
   ```

2. **Ajouter les fichiers du jeu**
   - Placer tous les fichiers `.java` dans `projet/<nom du jeu>/`
   - Placer les ressources (images, sons, etc.) dans des sous-dossiers si nécessaire

3. **Créer le script de lancement**
   - Créer un fichier `<nom du jeu>.sh` dans `projet/<nom du jeu>/`
   - Le script doit contenir les commandes pour lancer votre jeu

## Exemple de script de lancement

```bash
#!/bin/bash
cd "$(dirname "$0")"
java -cp "../.." <NomDeLaClassePrincipale>
```

## Compilation automatique

- La compilation est automatique au lancement de la borne
- Si vous ajoutez/modifiez des jeux, la compilation se lancera automatiquement
- Si aucun jeu n'est ajouté/supprimé, la compilation est sautée pour accélérer le démarrage

## Import MG2D

Pour utiliser la bibliothèque MG2D, assurez-vous d'avoir les bons imports :

```java
import MG2D.*;
import MG2D.geometrie.*;
import MG2D.Couleur;
```

> Vous n'avez pas à installer la bibliothèque MG2D, elle est déjà présente dans la borne et utiliser lors de la compilation

## Structure recommandée

```
projet/
└── <nom du jeu>/
    ├── JeuPrincipal.java
    ├── AutreClasse.java
    ├── <nom du jeu>.sh
    ├── img/
    ├── sounds/
    └── fonts/
```

## Notes importantes

- Le nom du dossier doit correspondre exactement au nom du script
- Les jeux sans fichiers Java seront listés mais ne pourront pas être compilés
- La borne détecte automatiquement les nouveaux jeux au prochain lancement

## Affichage des boutons

Pour permettre l'affichage des boutons dans la borne, vous devez créer un fichier `boutons.txt` dans le dossier `projet/<nom du jeu>/`.

### Exemple de bouton à ajouter

```txt
Mouvement DinoRail:aucun:aucun:Quitter:aucun:aucun:aucun:
```
> le texte entre les deux-points est le texte affiché sur le bouton et peut donc être n'importe quoi

## Pour les jeux en python

Pour les jeux en python, vous devez créer un fichier `requirements.txt` dans le dossier `projet/<nom du jeu>/`.