# Code Source

Cette section présente une vue d'ensemble du code source de la borne arcade.

## Architecture générale

Le projet est structuré autour de plusieurs classes principales qui gèrent l'interface graphique, les entrées utilisateur et la logique de sélection des jeux.

## Classes principales

### [Main](src/Main.md)
Point d'entrée de l'application. Initialise l'interface graphique et lance la boucle de sélection des jeux.

### [Graphique](src/Graphique.md)
Classe centrale qui gère :
- L'affichage du menu principal
- La navigation entre les jeux
- L'interface utilisateur complète
- La gestion des descriptions et high scores

### [ClavierBorneArcade](src/ClavierBorneArcade.md)
Gestionnaire des entrées spécifique à la borne arcade :
- Contrôles des joysticks (2 joueurs)
- Gestion des 6 boutons par joueur
- Détection d'appuis uniques et maintenus

### [BoiteSelection](src/BoiteSelection.md)
Gère la navigation dans le menu de sélection des jeux.

### [BoiteDescription](src/BoiteDescription.md)
Affiche les informations détaillées des jeux :
- Description du jeu
- Configuration des contrôles
- High scores

### [Bouton](src/Bouton.md)
Représente un bouton de jeu dans le menu principal.

### [Pointeur](src/Pointeur.md)
Gère le pointeur visuel de sélection dans le menu.

## Classes utilitaires

### [BoiteImage](src/BoiteImage.md)
Gère l'affichage des images dans l'interface.

> **Note** : Les classes `Boite`, `HighScore` et `LigneHighScore` ne sont pas documentées car les fichiers sources correspondants ne sont pas présents dans le répertoire `src/`.