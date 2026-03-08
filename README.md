# Borne Arcade - IUT du Littoral Côte d'Opale

Projet SAE - 3ème année BUT Informatique
15 jeux, menu de sélection Java, Raspberry Pi 3

**GUILMIN Leny | DAVID Gabriel**

---

## Matériel requis

- Raspberry Pi 3 (ou supérieur)
- Écran 4:3, résolution 1280x1024
- 2 joysticks + 6 boutons par joueur

---

## Installation

### 1. Cloner le repo

```bash
cd ~
mkdir git
git clone --recurse-submodules https://github.com/TarzanHR/arcade_maintenance.git ~/git
cd ~/git
```

### 2. Lancer le setup

```bash
bash setup.sh
```

Ce script fait tout automatiquement :
- Initialise les submodules (jeux externes comme CakeCraft)
- Télécharge et compile MG2D depuis GitHub
- Installe les dépendances système (Java, Python, LÖVE, etc.)
- Installe le layout clavier personnalisé
- Compile le menu et les jeux
- Configure le lancement automatique au démarrage

---

## Lancement

Au démarrage du bureau, la borne se lance automatiquement.
Pour la lancer manuellement :

```bash
cd /home/pi/git/borne_arcade
bash lancerBorne.sh
```

Un écran de chargement s'affiche pendant la compilation, puis le menu apparaît.

---

## Contrôles

| Action | Joueur 1 | Joueur 2 |
|--------|----------|----------|
| Joystick | Flèches directionnelles | O / L / K / M |
| Boutons rangée haute | R T Y | A Z E |
| Boutons rangée basse | F G H | Q S D |

> Le layout clavier personnalisé (`borne`) remplace les touches `1 2 3 4 5 6` par `r t y f g h` pour correspondre aux boutons physiques de la borne.

---

## Structure du repo

```
/home/pi/git/
├── setup.sh                  # Point d'entrée installation
├── create_mg2d_jar.sh        # Compile MG2D depuis GitHub
├── ollama_wrapper.py         # Interface Ollama pour les outils IA
└── borne_arcade/
    ├── install.sh            # Orchestrateur installation (7 étapes)
    ├── lancerBorne.sh        # Lancement de la borne
    ├── compilation.sh        # Compilation Java
    ├── src/                  # Code source du menu Java
    ├── projet/               # Jeux (Java, Python, Lua)
    ├── assets/               # Fonts, images, sons
    ├── config/               # Chemins et configuration
    ├── tools/                # Scripts outils
    ├── scripts/              # Scripts utilitaires et CI/CD
    └── ArcadeDocs/           # Documentation MkDocs
```

---

## Ajouter un jeu

Voir la documentation en ligne : https://tarzanhr.github.io/arcade_maintenance/ajout_jeu/

---

## Documentation

La documentation est générée automatiquement et déployée sur GitHub Pages à chaque push sur `main`.

Pour la consulter localement :

```bash
cd ArcadeDocs
mkdocs serve --dev-addr=0.0.0.0:8001
```

---

## Mise à jour de la borne

```bash
cd /home/pi/git/borne_arcade
bash update.sh
```

---

## Documentation complète

Pour en savoir plus, consultez la documentation en ligne : https://tarzanhr.github.io/arcade_maintenance/

---

## Extinction

Quitter le menu avec le bouton **Y** du joueur 1 (touche `3` sur clavier AZERTY standard, `y` après layout borne). Un compte à rebours de 30 secondes s'affiche puis la machine s'éteint automatiquement.
