# Guide d'ajout de jeux

Ce guide explique comment ajouter de nouveaux jeux à la borne arcade.

## Prérequis

- Connaissance de base en programmation Java
- Compréhension de la bibliothèque MG2D
- Les jeux doivent utiliser les contrôles standards de la borne

## Structure d'un jeu

### Classe principale

Chaque jeu doit avoir une classe principale qui hérite des fonctionnalités de base de la borne :

```java
import java.awt.*;
import java.awt.event.*;
import mg2d.*;

public class MonJeu {
    private boolean jeuEnCours = true;
    private ClavierBorneArcade clavier;
    
    public MonJeu(ClavierBorneArcade clavier) {
        this.clavier = clavier;
        initialiserJeu();
    }
    
    private void initialiserJeu() {
        // Initialisation du jeu
    }
    
    public void jouer() {
        while (jeuEnCours) {
            // Logique du jeu
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
        // Gestion des entrées clavier
        if (clavier.getATape()) {
            // Action bouton A
        }
        if (clavier.getHautTape()) {
            // Action haut
        }
        // ... autres contrôles
    }
    
    private void mettreAJour() {
        // Logique du jeu
    }
    
    private void dessiner() {
        // Rendu graphique
    }
}
```

## Étapes d'ajout d'un jeu

### 1. Créer le répertoire du jeu

```bash
cd /home/pi/git/borne_arcade
mkdir jeux/mon_jeu
```

### 2. Développer le jeu

Créez les fichiers Java dans le répertoire `jeux/mon_jeu/` :

```
jeux/mon_jeu/
├── MonJeu.java          # Classe principale
├── Personnage.java     # Classes additionnelles
├── Niveau.java
└── assets/             # Ressources du jeu
    ├── images/
    └── sons/
```

### 3. Compiler le jeu

```bash
cd jeux/mon_jeu
javac -cp ../../src:. *.java
```

### 4. Ajouter le jeu à la liste

Modifiez le fichier `data/noms_jeux.txt` :

```
Jeu1
Jeu2
MonJeu
```

### 5. Intégrer dans le système principal

Modifiez la classe `Graphique.java` pour inclure votre jeu dans la logique de sélection :

```java
// Dans la méthode selectionJeu()
if (selection.equals("MonJeu")) {
    MonJeu jeu = new MonJeu(this.clavier);
    jeu.jouer();
}
```

## Bonnes pratiques

### Contrôles normalisés

Utilisez les contrôles standards définis dans `ClavierBorneArcade` :

```java
// Mouvements
clavier.getHaut(), clavier.getBas(), clavier.getGauche(), clavier.getDroite()

// Boutons action
clavier.getA(), clavier.getB(), clavier.getC()
clavier.getX(), clavier.getY(), clavier.getZ()

// Détection d'appui unique
clavier.getHautTape(), clavier.getATape(), etc.
```

### Gestion des ressources

Placez les ressources dans un sous-dossier `assets/` :

```java
// Chargement d'images
Image image = Toolkit.getDefaultToolkit().getImage("assets/images/personnage.png");

// Chargement de sons (si applicable)
// Utiliser java.applet.AudioClip ou autre bibliothèque audio
```

### Performance

- Maintenez 60 FPS (16ms par frame)
- Évitez les allocations d'objets dans la boucle principale
- Utilisez des techniques d'optimisation graphique

### Sortie du jeu

Prévoyez toujours un moyen de quitter le jeu :

```java
if (clavier.getATape() && clavier.getXTape()) {
    // Combinaison pour quitter
    jeuEnCours = false;
}
```

## Test du jeu

### Test manuel

```bash
cd /home/pi/git/borne_arcade
java -cp src:jeux/mon_jeu Main
```

### Test des contrôles

Vérifiez que tous les contrôles fonctionnent correctement :
- Mouvements dans toutes les directions
- Tous les boutons répondent
- La combinaison de sortie fonctionne

## Déploiement

Une fois le jeu testé et fonctionnel :

1. **Version finale** : Nettoyez le code et ajoutez des commentaires
2. **Documentation** : Créez un README spécifique au jeu
3. **Tests** : Faites tester le jeu par plusieurs utilisateurs
4. **Intégration** : Ajoutez-le officiellement à la borne

## Exemple complet

Voici un exemple simple de jeu Pong :

```java
import java.awt.*;
import mg2d.*;

public class PongSimple {
    private boolean enCours = true;
    private ClavierBorneArcade clavier;
    private int raquette1Y = 200, raquette2Y = 200;
    private int balleX = 400, balleY = 300;
    private int vitesseBalleX = 3, vitesseBalleY = 2;
    
    public PongSimple(ClavierBorneArcade clavier) {
        this.clavier = clavier;
    }
    
    public void jouer() {
        while (enCours) {
            traiterEntrees();
            mettreAJour();
            dessiner();
            
            try {
                Thread.sleep(16);
            } catch (InterruptedException e) {}
        }
    }
    
    private void traiterEntrees() {
        // Joueur 1 (Q/S pour haut/bas)
        if (clavier.getQ()) raquette1Y -= 5;
        if (clavier.getS()) raquette1Y += 5;
        
        // Joueur 2 (Flèches pour haut/bas)
        if (clavier.getHaut()) raquette2Y -= 5;
        if (clavier.getBas()) raquette2Y += 5;
        
        // Quitter avec ESC
        if (clavier.getATape()) enCours = false;
    }
    
    private void mettreAJour() {
        balleX += vitesseBalleX;
        balleY += vitesseBalleY;
        
        // Rebonds sur les murs haut/bas
        if (balleY <= 0 || balleY >= 600) vitesseBalleY = -vitesseBalleY;
        
        // Rebonds sur les raquettes
        if (balleX <= 50 && balleY >= raquette1Y && balleY <= raquette1Y + 100) {
            vitesseBalleX = -vitesseBalleX;
        }
        if (balleX >= 750 && balleY >= raquette2Y && balleY <= raquette2Y + 100) {
            vitesseBalleX = -vitesseBalleX;
        }
        
        // Limites des raquettes
        raquette1Y = Math.max(0, Math.min(500, raquette1Y));
        raquette2Y = Math.max(0, Math.min(500, raquette2Y));
    }
    
    private void dessiner() {
        // Logique de dessin avec MG2D
        // À implémenter selon la bibliothèque graphique utilisée
    }
}
```
