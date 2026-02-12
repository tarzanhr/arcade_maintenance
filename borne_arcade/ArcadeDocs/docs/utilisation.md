# Guide d'utilisation de la Borne Arcade

Ce guide explique comment utiliser la borne arcade, lancer les jeux et gérer le système.

## Démarrage de la borne

### Lancement automatique

Pour configurer le démarage automatique, utilisez la commande :

```bash
cd /home/pi/git/borne_arcade
./install.sh
```

### Lancement manuel

Pour lancer la borne manuellement, utilisez le script dédié :

```bash
cd /home/pi/git/borne_arcade
./lancerBorne.sh
```

Le script `lancerBorne.sh` effectue les opérations suivantes :
1. Configure le clavier spécifique de la borne (`setxkbmap borne`)
2. Nettoie les fichiers temporaires (`./clean.sh`)
3. Compile le menu et tous les jeux (`./compilation.sh`)
4. Lance l'application principale (`java -cp "bin:$JAVA_CP" Main`)

### Lancement direct (développement)

Pour un lancement rapide sans compilation complète :

```bash
cd /home/pi/git/borne_arcade
java -cp "bin:$JAVA_CP" Main
```

## Processus de démarrage détaillé

### 1. Configuration du clavier

```bash
setxkbmap borne
```

Configure la disposition des touches spécifique à la borne arcade.

### 2. Nettoyage

Le script `clean.sh` supprime :
- Les fichiers compilés (`bin/*`)
- Les fichiers temporaires (`*~`)
- Les classes compilées des jeux (`projet/*/*.class`)

### 3. Compilation

Le script `compilation.sh` effectue :

**Compilation du menu principal** :
```bash
mkdir -p bin
javac -d bin -cp "$JAVA_CP" src/*.java
```

**Compilation des jeux** :
```bash
cd projet
for i in *; do
    cd $i
    if ls *.java 1> /dev/null 2>&1; then
        javac -cp "$JAVA_CP:../../bin:../.." *.java
    fi
    cd ..
done
```

**Génération de la liste des jeux** :
```bash
./scripts/liste_jeux.sh > data/noms_jeux.txt
```

**Permissions des scripts** :
```bash
./scripts/set_executable.sh
```

## Arrêt de la borne

### Arrêt propre

Pour arrêter la borne proprement :
2. Utilisez le bouton "Quitter" (sur PC le bouton Y) dans le menu pour quitter
3. Le script `lancerBorne.sh` peut être configuré pour éteindre le système automatiquement

### Arrêt système

L'arrêt système est géré par le script `lancerBorne.sh` et ferme la borne après avoir fermé le menu de la borne.

## Interface utilisateur

### Navigation principale

- **Joystick** : Navigation dans le menu (haut/bas)
- **Bouton A** : Sélectionner et lancer un jeu
- **Bouton Z** : Menu de confirmation pour quitter
- **ESC** : Retour au menu principal depuis un jeu

### Contrôles par défaut

| Action | Joueur 1 | Joueur 2 |
|--------|-----------|-----------|
| Haut | Flèche haut | O |
| Bas | Flèche bas | L |
| Gauche | Flèche gauche | K |
| Droite | Flèche droite | M |
| Bouton A | R | A |
| Bouton B | T | Z |
| Bouton C | Y | E |
| Bouton X | F | Q |
| Bouton Y | G | S |
| Bouton Z | H | D |

## Scripts utilitaires

### Liste des jeux

Pour voir tous les jeux disponibles :
```bash
./scripts/liste_jeux.sh
```

### Permissions

Pour donner les permissions d'exécution à tous les scripts de jeux :
```bash
./scripts/set_executable.sh
```

### Mise à jour

Pour mettre à jour le projet :
```bash
./update.sh
```