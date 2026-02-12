# Générateur de Documentation MkDocs

Ce projet inclut un générateur automatique de documentation qui analyse les fichiers Java source et crée une documentation structurée pour MkDocs.

## Utilisation

### Générer la documentation

```bash
cd /home/pi/git/borne_arcade
python3 generate_docs.py
```

### Construire le site MkDocs

```bash
cd /home/pi/git/borne_arcade/ArcadeDocs
mkdocs build
```

### Servir le site localement

```bash
cd /home/pi/git/borne_arcade/ArcadeDocs
mkdocs serve
```

Le site sera accessible à l'adresse `http://127.0.0.1:8000`

## Fonctionnalités

Le générateur analyse automatiquement :

- **Classes** : Documentation principale de chaque classe
- **Méthodes** : Documentation de chaque méthode avec ses paramètres
- **Attributs** : Documentation des champs et variables
- **Navigation** : Structure automatique dans mkdocs.yml

## Structure générée

```
ArcadeDocs/
├── mkdocs.yml              # Configuration MkDocs générée
└── docs/
    ├── index.md           # Page d'accueil
    ├── utilisation.md     # Guide d'utilisation de la borne
    ├── ajout_jeu.md       # Guide pour ajouter des jeux
    ├── mg2d.md           # Guide d'importation MG2D
    ├── scripts.md        # Documentation des scripts
    └── src/               # Documentation du code source
        ├── Main.md        # Documentation de Main
        ├── Graphique.md   # Documentation de Graphique
        ├── ClavierBorneArcade.md  # Documentation de ClavierBorneArcade
        └── ...            # Autres classes
```

## Personnalisation

Pour modifier le générateur, éditez le fichier `generate_docs.py` :

- `parse_java_file()` : Analyse des fichiers Java
- `generate_class_doc()` : Formatage de la documentation
- `update_mkdocs_config()` : Configuration MkDocs

## Prérequis

- Python 3
- MkDocs : `pip install mkdocs`
- Thème Material (optionnel) : `pip install mkdocs-material`
