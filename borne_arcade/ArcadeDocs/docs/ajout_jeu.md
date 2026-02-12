# Guide d'ajout de jeux

Ce guide explique comment ajouter de nouveaux jeux à la borne arcade.

## Prérequis

- Connaissance de base en programmation Java
- Compréhension de la bibliothèque MG2D
- Les jeux doivent utiliser les contrôles standards de la borne

## Structure d'un jeu

### Analyse du code source

D'après l'analyse du code source de la borne (`Graphique.java`, `Bouton.java`, `Pointeur.java`), voici comment fonctionne réellement l'ajout de jeux :

1. **Découverte automatique** : La borne scanne le répertoire `projet/` pour découvrir les jeux
2. **Création des boutons** : Chaque sous-dossier de `projet/` devient un bouton dans le menu
3. **Lancement par script** : Chaque jeu doit avoir un script `.sh` avec le même nom que le dossier

### Classe principale

Chaque jeu doit avoir une classe principale qui utilise les contrôles de la borne :

```java
import java.awt.*;
import java.awt.event.*;
import mg2d.*;

public class MonJeu {
    private boolean jeuEnCours = true;
    private ClavierBorneArcade clavier;
    
    public MonJeu() {
        // Le clavier est géré par la borne, pas besoin de le créer
        initialiserJeu();
    }
    
    public static void main(String[] args) {
        MonJeu jeu = new MonJeu();
        jeu.jouer();
    }
    
    public void jouer() {
        while (jeuEnCours) {
            traiterEntrees();
            mettreAJour();
            dessiner();
            
            try {
                Thread.sleep(16); // ~60 FPS
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    
    private void traiterEntrees() {
        // Utiliser les contrôles via System.in ou autre méthode
        // selon l'implémentation spécifique
    }
}
```

## Étapes d'ajout d'un jeu

### 1. Créer le répertoire du jeu

```bash
cd /home/pi/git/borne_arcade
mkdir projet/mon_jeu
```

### 2. Développer le jeu

Créez les fichiers Java dans le répertoire `projet/mon_jeu/` :

```
projet/mon_jeu/
├── MonJeu.java          # Classe principale
├── Personnage.java     # Classes additionnelles
├── Niveau.java
├── assets/             # Ressources du jeu
│   ├── images/
│   └── sons/
├── description.txt     # Description du jeu (affichée dans le menu)
├── bouton.txt         # Configuration des boutons (obligatoire)
├── highscore          # Fichier de high scores (créé automatiquement)
├── image.png          # Image de prévisualisation (optionnel)
├── photo.png          # Photo du jeu (optionnel)
└── photo_small.png    # Petite vignette (optionnel)
```
> ce n'est qu'un exemple, vous pouvez faire la structure que vous voulez le temps que le script de lancement, bouton.txt, image.png, photo.png et photo_small.png soient présents à la racine du jeu.

### 3. Créer le script de lancement

Créez un fichier `<nom du jeu>.sh` dans le répertoire du jeu
Choisissez le type de script selon votre technologie :

**Pour les jeux Java avec MG2D** :
```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cd "$BORNE_ROOT/projet/<nom_du_jeu>"
java -cp ".:../..:$BORNE_ROOT/bin:$MG2D_JAR" <ClassePrincipale>
```
> Si vous n'utilisez pas MG2D, vous n'avez pas à l'importer dans le script de lancement.

**Pour les jeux Python** :
```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cd "$BORNE_ROOT/projet/<nom_du_jeu>"
python3 app/game.py
```

> Si vous utilisez des bibliothèques externes, vous devez mettre un requirement.txt à la racine du jeu.

**Pour les jeux LÖVE (Lua)** :
```bash
#!/bin/bash
source "$(dirname "$0")/common.sh"
cd "$BORNE_ROOT/projet/<nom_du_jeu>"
love .
```

### 4. Créer les fichiers de description

**description.txt** (obligatoire) :
```
MonJeu - Votre Nom - 2025

Description courte du jeu qui sera affichée
dans le menu de la borne arcade.

Crédits:
auteur1 (pour la contribution1)
auteur2 (pour la contribution2)
```

**bouton.txt** (obligatoire) :
Le format est : `TexteJoystick:TexteBoutonA:TexteBoutonB:TexteBoutonC:TexteBoutonX:TexteBoutonY:TexteBoutonZ:`

### 5. Détection automatique

La borne détecte automatiquement les nouveaux jeux :
- Au démarrage, elle scanne le répertoire `projet/`
- Chaque sous-dossier devient un bouton dans le menu
- Le nom du dossier devient le nom affiché dans le menu
- Le script `.sh` est utilisé pour lancer le jeu

### 6. Import MG2D

Pour utiliser la bibliothèque MG2D, ajoutez les imports en haut de vos fichiers Java :

```java
import mg2d.*;
import mg2d.geometrie.*;
import java.awt.*;
```

> **Important** : MG2D est déjà installée sur la borne et accessible via `$MG2D_JAR`

## Notes importantes

- Le nom du dossier doit correspondre exactement au nom du script `.sh`
- Le fichier `description.txt` est obligatoire pour afficher une description dans le menu
- Le fichier `bouton.txt` est obligatoire pour afficher les contrôles dans le menu
- Le fichier `highscore` est créé automatiquement mais doit exister pour éviter les erreurs
- La borne détecte automatiquement les nouveaux jeux au prochain lancement/redémarrage
- Les images `image.png`, `photo.png` et `photo_small.png` sont utilisées pour l'affichage dans le menu

## Technologies supportées

### Java + MG2D (recommandé)
- **Avantages** : Performant, bien intégré avec la borne
- **Utilisation** : `java -cp ".:../..:$BORNE_ROOT/bin:$MG2D_JAR" Main`
- **Exemples** : Pong, Snake, Columns, DinoRail, JavaSpace, Minesweeper

### Python 3
- **Avantages** : Facile à développer, nombreuses bibliothèques
- **Utilisation** : `python3 app/game.py` ou `"$BORNE_ROOT/tools/python_wrapper.sh" main.py`
- **Exemples** : PianoTile, TronGame

### LÖVE (Lua)
- **Avantages** : Framework 2D complet, bonne performance
- **Utilisation** : `love .`
- **Exemples** : CursedWare

## Bonnes pratiques

### Contrôles de la borne

La borne utilise `ClavierBorneArcade` pour gérer les entrées. Dans vos jeux, vous pouvez :

1. **Utiliser les contrôles standards** via les méthodes de `ClavierBorneArcade`
2. **Créer votre propre gestionnaire** si vous hébergez `ClavierBorneArcade.java` dans votre jeu

### Sortie du jeu

Prévoyez un moyen de quitter le jeu pour retourner au menu :

```java
// Exemple : touche ESC ou combinaison de boutons
if (toucheQuitter) {
    System.exit(0); // Retour au menu de la borne
}
```

## Exemple complet basé sur DinoRail

Voici un exemple simplifié basé sur le jeu DinoRail existant :

```java
import mg2d.*;
import mg2d.geometrie.*;
import java.awt.*;

public class MonJeu {
    private Fenetre f;
    private boolean jeuEnCours = true;
    
    public MonJeu() {
        f = new Fenetre("Mon Jeu", 800, 600);
        f.setVisible(true);
    }
    
    public void jouer() {
        while (jeuEnCours) {
            traiterEntrees();
            mettreAJour();
            dessiner();
            
            try {
                Thread.sleep(16);
            } catch (InterruptedException e) {}
        }
        
        f.dispose();
    }
    
    private void traiterEntrees() {
        // Gestion des entrées clavier/souris
        // selon les besoins du jeu
    }
    
    private void mettreAJour() {
        // Logique du jeu
    }
    
    private void dessiner() {
        f.effacer();
        
        // Dessiner les éléments du jeu
        Rectangle joueur = new Rectangle(Couleur.BLEU, new Point(100, 100), 50, 50);
        f.ajouter(joueur);
        
        f.rafraichir();
    }
    
    public static void main(String[] args) {
        MonJeu jeu = new MonJeu();
        jeu.jouer();
    }
}
```

## Dépannage

### Problèmes courants

1. **Le jeu n'apparaît pas dans le menu**
   - Vérifiez que le dossier est dans `projet/`
   - Vérifiez que le script `.sh` existe et est exécutable et à le nom du projet
   - Vérifiez que `description.txt` existe
   - Redémarrez la borne

2. **Erreur de compilation Java**
   - Vérifiez le classpath dans le script `.sh`
   - Assurez-vous que MG2D est accessible via `$MG2D_JAR`
   - Vérifiez les imports dans vos fichiers Java
   - Certains jeux nécessitent des options JVM spéciales

3. **Problèmes d'affichage**
   - Vérifiez que `xdotool mousemove 1280 1024` est dans le script
   - Testez avec différentes résolutions
   - Vérifiez que les ressources sont accessibles

4. **Jeux Python/LÖVE ne fonctionnent pas**
   - Vérifiez que Python 3 ou LÖVE est installé sur la borne
   - Vérifiez les permissions des scripts
   - Testez manuellement depuis le terminal

### Vérification par technologie

**Test manuel Java** :
```bash
cd projet/mon_jeu
java -cp ".:../..:/home/pi/git/MG2D.jar" MonJeu
```

**Test manuel Python** :
```bash
cd projet/mon_jeu
python3 app/game.py
```

**Test manuel LÖVE** :
```bash
cd projet/mon_jeu
love .
```