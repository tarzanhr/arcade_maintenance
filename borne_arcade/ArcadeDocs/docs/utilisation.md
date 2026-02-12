# Guide d'utilisation de la Borne Arcade

Ce guide explique comment utiliser la borne arcade, lancer les jeux et gérer le système.

## Démarrage de la borne

### Lancement automatique

La borne est configurée pour démarrer automatiquement au boot du Raspberry Pi. Le système lance automatiquement l'application principale.

### Lancement manuel

Pour lancer la borne manuellement depuis un terminal :

```bash
cd /home/pi/git/borne_arcade
java Main
```

### Arrêt de la borne

Pour arrêter proprement la borne :

1. Appuyez sur `Ctrl+C` dans le terminal si lancé manuellement
2. Ou utilisez le bouton d'arrêt système si configuré

## Interface utilisateur

### Navigation principale

L'interface principale permet de :
- **Sélectionner un jeu** avec les flèches directionnelles
- **Lancer un jeu** avec le bouton A (validation)
- **Revenir au menu** avec le bouton ESC pendant un jeu

### Contrôles par défaut

| Action | Joueur 1 | Joueur 2 |
|--------|-----------|-----------|
| Haut | Flèche haut | Z |
| Bas | Flèche bas | S |
| Gauche | Flèche gauche | Q |
| Droite | Flèche droite | D |
| Bouton A | A | W |
| Bouton B | B | X |
| Bouton C | C | V |
| Bouton X | E | R |
| Bouton Y | F | T |
| Bouton Z | G | Y |

## Gestion des jeux

### Structure des jeux

Les jeux sont organisés dans le répertoire du projet :

```
borne_arcade/
├── src/                    # Code source des classes principales
├── jeux/                   # Répertoire des jeux (à créer)
│   ├── jeu1/
│   ├── jeu2/
│   └── ...
└── data/
    └── noms_jeux.txt       # Liste des jeux disponibles
```

### Fichier de configuration des jeux

Le fichier `data/noms_jeux.txt` contient la liste des jeux disponibles :

```
Jeu1
Jeu2
Jeu3
```

Chaque ligne correspond à un jeu qui apparaîtra dans le menu de sélection.
