# Analyse de Jeux

La borne arcade dispose d'outils d'analyse IA pour générer des présentations détaillées des jeux.

## Scripts disponibles

### 1. Analyse individuelle de jeu

**Fichier** : `scripts/analyze_single_game.py`

Analyse un seul jeu et génère une présentation complète avec l'IA.

```bash
# Lister les jeux disponibles
python3.14 scripts/analyze_single_game.py --list

# Analyser un jeu spécifique
python3.14 scripts/analyze_single_game.py --game Pong

# Avec un modèle IA différent
python3.14 scripts/analyze_single_game.py --game Pong --model qwen2:latest
```

**Fonctionnalités** :
- Extraction des données brutes du jeu (fichiers sources, README, requirements)
- Génération d'une présentation attractive par IA
- Format Markdown sans emojis
- Logs détaillés en temps réel
- Sauvegarde dans `game_presentations/`

**Résultat** : Fichier Markdown avec présentation complète du jeu

---

### 2. Analyse batch de tous les jeux

**Fichier** : `scripts/analyze_games.py`

Analyse tous les jeux du dossier `projet/` en séquence.

```bash
# Lister les jeux disponibles
python3.14 scripts/analyze_games.py --list

# Analyser tous les jeux (délai de 2s entre chaque)
python3.14 scripts/analyze_games.py

# Analyse rapide sans délai
python3.14 scripts/analyze_games.py --delay 0

# Avec modèle IA personnalisé
python3.14 scripts/analyze_games.py --model gemma2:latest --delay 3
```

**Fonctionnalités** :
- Analyse séquentielle de tous les jeux
- Utilise le script d'analyse individuelle pour chaque jeu
- Génération d'un rapport récapitulatif
- Gestion des erreurs individuelles
- Durée totale estimée

**Résultats** :
- Fichiers individuels dans `game_presentations/`
- Rapport récapitulatif dans `batch_analysis_summary.md`

---

## Configuration requise

### Dépendances
- Python 3.11+
- Ollama (installé et fonctionnel)
- Accès réseau au serveur Ollama

### Modèles IA compatibles
- `gemma2:latest` (recommandé)
- `qwen2:latest`
- Autres modèles Ollama compatibles

### Timeout
Le timeout Ollama est configuré à 120 secondes pour les analyses longues.

---

## Structure des fichiers générés

### Présentations individuelles
```
game_presentations/
├── presentation_columns.md
├── presentation_pong.md
├── presentation_minesweeper.md
└── ...
```

Chaque fichier contient :
- Métadonnées (jeu, date, modèle, durée)
- Présentation générée par l'IA avec sections :
  - Description
  - Objectif du jeu
  - Comment jouer
  - Points forts
  - Aspect technique
  - Pour qui ?
  - Note finale

### Rapport batch
```
batch_analysis_summary.md
```

Contient :
- Statistiques globales
- Détail par jeu (succès/erreurs)
- Liste des fichiers générés
- Durée totale

---

## Exemples d'utilisation

### Analyser un seul jeu
```bash
cd /home/pi/git/borne_arcade
python3.14 scripts/analyze_single_game.py --game Minesweeper
```

Résultat attendu :
```
🎮===========================================================
🎮  ANALYSE DU JEU: Minesweeper
🎮===========================================================
📂 Chemin du jeu: /home/pi/git/borne_arcade/projet/Minesweeper
🤖 Modèle IA: gemma2:latest

[1/4] 📂 Extraction des données brutes...
   📖 Fichier README trouvé: README.md
   ✅ 99 fichiers extraits

[2/4] 📝 Création du prompt de présentation...
   ✅ Prompt de présentation de 2906 caractères créé

[3/4] 🤖 Génération de la présentation...
   ✅ Présentation générée en 45.2s

[4/4] 💾 Sauvegarde de la présentation...
   ✅ Présentation sauvegardée: game_presentations/presentation_minesweeper.md
```

### Analyser tous les jeux
```bash
cd /home/pi/git/borne_arcade
python3.14 scripts/analyze_games.py --delay 1
```

Analysera les 14 jeux avec un délai de 1 seconde entre chaque.

---

## Dépannage

### Problèmes courants

**Timeout Ollama**
- Augmenter le timeout dans `ollama_wrapper.py`
- Vérifier la connexion au serveur Ollama

**Jeu non trouvé**
- Vérifier que le jeu existe dans `projet/`
- Utiliser `--list` pour voir les jeux disponibles

**Erreur d'extraction**
- Vérifier les permissions sur les fichiers
- Certains jeux peuvent avoir des structures inhabituelles

### Logs détaillés

Les scripts fournissent des logs détaillés avec :
- Progression en temps réel
- Nombre de fichiers extraits
- Durée de chaque étape
- Erreurs spécifiques

---

## Notes techniques

### Architecture
- `analyze_single_game.py` : Analyse individuelle
- `analyze_games.py` : Batch utilisant l'analyse individuelle
- `ollama_wrapper.py` : Interface avec Ollama

### Personnalisation
Les prompts peuvent être modifiés dans les scripts pour changer :
- Style de présentation
- Sections demandées
- Format de sortie

### Performance
- Temps moyen par jeu : 3-5 minutes