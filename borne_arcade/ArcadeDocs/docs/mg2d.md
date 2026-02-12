# Guide d'importation de MG2D

Ce guide explique comment importer et utiliser la bibliothèque MG2D dans le projet Borne Arcade.

## Qu'est-ce que MG2D ?

MG2D (MiniGraphics2D) est une bibliothèque graphique Java simplifiée développée pour l'IUT de Calais. Elle facilite la création d'interfaces graphiques 2D et de jeux simples.

## Installation de MG2D

### Méthode 1 : Téléchargement direct

1. **Télécharger MG2D**
   ```bash
   cd /home/pi/git/borne_arcade
   wget http://www.iut-calais.info/mg2d/mg2d.jar
   ```

2. **Créer le répertoire lib**
   ```bash
   mkdir -p lib
   mv mg2d.jar lib/
   ```

### Méthode 2 : Compilation depuis les sources

1. **Cloner le dépôt MG2D**
   ```bash
   cd /home/pi/git
   git clone https://github.com/iut-calais/mg2d.git
   cd mg2d
   ```

2. **Compiler la bibliothèque**
   ```bash
   javac src/mg2d/*.java
   jar cf mg2d.jar -C src/ .
   cp mg2d.jar ../borne_arcade/lib/
   ```

## Configuration du projet

### Mettre à jour le classpath

Modifiez les scripts de compilation pour inclure MG2D :

**Script de compilation manuel**
```bash
#!/bin/bash
javac -cp lib/mg2d.jar:src src/*.java
java -cp lib/mg2d.jar:src Main
```

**Script de compilation avec les jeux**
```bash
#!/bin/bash
javac -cp lib/mg2d.jar:src:jeux/* src/*.java jeux/*/*.java
java -cp lib/mg2d.jar:src:jeux/* Main
```

### Fichier build.xml (Ant)

Si vous utilisez Ant pour la compilation :

```xml
<path id="classpath">
    <fileset dir="lib" includes="*.jar"/>
    <pathelement location="src"/>
    <pathelement location="jeux"/>
</path>

<target name="compile">
    <javac srcdir="src" destdir="build" classpathref="classpath"/>
    <javac srcdir="jeux" destdir="build" classpathref="classpath"/>
</target>
```

## Utilisation de base de MG2D

### Importation des classes

```java
import mg2d.*;
import mg2d.geometrie.*;
import java.awt.*;
```

### Création d'une fenêtre

```java
public class MonJeu {
    private Fenetre fenetre;
    
    public MonJeu() {
        fenetre = new Fenetre("Mon Jeu", 800, 600);
        fenetre.setDefaultCloseOperation(Fenetre.EXIT_ON_CLOSE);
    }
}
```

### Dessin d'objets

```java
public void dessiner() {
    // Effacer l'écran
    fenetre.effacer();
    
    // Dessiner un rectangle
    Rectangle rect = new Rectangle(100, 100, 50, 50);
    fenetre.dessiner(rect, Color.RED);
    
    // Dessiner un cercle
    Cercle cercle = new Cercle(200, 200, 25);
    fenetre.dessiner(cercle, Color.BLUE);
    
    // Dessiner du texte
    fenetre.dessiner("Score: 100", 10, 10, Color.WHITE);
    
    // Mettre à jour l'affichage
    fenetre.mettreAJour();
}
```

### Gestion des événements

```java
public class MonJeu implements KeyListener {
    private Fenetre fenetre;
    
    public MonJeu() {
        fenetre = new Fenetre("Mon Jeu", 800, 600);
        fenetre.addKeyListener(this);
    }
    
    @Override
    public void keyPressed(KeyEvent e) {
        int code = e.getKeyCode();
        
        switch(code) {
            case KeyEvent.VK_UP:
                // Action flèche haut
                break;
            case KeyEvent.VK_DOWN:
                // Action flèche bas
                break;
            case KeyEvent.VK_SPACE:
                // Action espace
                break;
        }
    }
    
    @Override
    public void keyReleased(KeyEvent e) {}
    
    @Override
    public void keyTyped(KeyEvent e) {}
}
```

## Intégration avec la borne arcade

### Adaptation pour les contrôles de la borne

```java
import mg2d.*;
import java.awt.*;

public class JeuBorne {
    private Fenetre fenetre;
    private ClavierBorneArcade clavier;
    
    public JeuBorne(ClavierBorneArcade clavier) {
        this.clavier = clavier;
        fenetre = new Fenetre("Jeu Borne", 800, 600);
        fenetre.setFullscreen(true); // Mode plein écran pour la borne
    }
    
    public void jouer() {
        boolean enCours = true;
        
        while (enCours) {
            traiterEntrees();
            mettreAJour();
            dessiner();
            
            try {
                Thread.sleep(16); // 60 FPS
            } catch (InterruptedException e) {}
        }
        
        fenetre.dispose();
    }
    
    private void traiterEntrees() {
        // Utiliser les contrôles de la borne
        if (clavier.getHaut()) {
            // Déplacement vers le haut
        }
        if (clavier.getA()) {
            // Action bouton A
        }
        if (clavier.getATape()) {
            // Détection d'appui unique
        }
    }
    
    private void mettreAJour() {
        // Logique du jeu
    }
    
    private void dessiner() {
        fenetre.effacer();
        
        // Dessiner les éléments du jeu
        Rectangle joueur = new Rectangle(100, 100, 50, 50);
        fenetre.dessiner(joueur, Color.GREEN);
        
        fenetre.mettreAJour();
    }
}
```

## Classes principales de MG2D

### Fenêtre

```java
Fenetre fenetre = new Fenetre("Titre", largeur, hauteur);
fenetre.setFullscreen(true);        // Plein écran
fenetre.setResizable(false);        // Non redimensionnable
fenetre.setBackground(Color.BLACK); // Couleur de fond
fenetre.mettreAJour();              // Rafraîchir l'affichage
fenetre.effacer();                  // Effacer l'écran
```

### Formes géométriques

```java
// Rectangle
Rectangle rect = new Rectangle(x, y, largeur, hauteur);

// Cercle
Cercle cercle = new Cercle(centreX, centreY, rayon);

// Ligne
Ligne ligne = new Ligne(x1, y1, x2, y2);

// Texte
fenetre.dessiner("Texte", x, y, couleur);
```

### Images

```java
// Charger une image
Image image = Toolkit.getDefaultToolkit().getImage("chemin/image.png");

// Dessiner une image
fenetre.dessiner(image, x, y);
fenetre.dessiner(image, x, y, largeur, hauteur);
```

## Exemple complet

Voici un exemple complet de jeu simple utilisant MG2D :

```java
import mg2d.*;
import java.awt.*;
import java.awt.event.*;

public class ExempleJeu implements KeyListener {
    private Fenetre fenetre;
    private int joueurX = 400, joueurY = 300;
    private boolean enCours = true;
    
    public ExempleJeu() {
        fenetre = new Fenetre("Exemple Jeu", 800, 600);
        fenetre.addKeyListener(this);
        fenetre.setBackground(Color.BLACK);
    }
    
    public void jouer() {
        while (enCours) {
            dessiner();
            
            try {
                Thread.sleep(16);
            } catch (InterruptedException e) {}
        }
        
        fenetre.dispose();
    }
    
    private void dessiner() {
        fenetre.effacer();
        
        // Dessiner le joueur
        Rectangle joueur = new Rectangle(joueurX, joueurY, 30, 30);
        fenetre.dessiner(joueur, Color.WHITE);
        
        // Dessiner des informations
        fenetre.dessiner("Position: (" + joueurX + ", " + joueurY + ")", 10, 10, Color.WHITE);
        fenetre.dessiner("ESC pour quitter", 10, 30, Color.GRAY);
        
        fenetre.mettreAJour();
    }
    
    @Override
    public void keyPressed(KeyEvent e) {
        int vitesse = 5;
        
        switch(e.getKeyCode()) {
            case KeyEvent.VK_UP:
                joueurY = Math.max(0, joueurY - vitesse);
                break;
            case KeyEvent.VK_DOWN:
                joueurY = Math.min(570, joueurY + vitesse);
                break;
            case KeyEvent.VK_LEFT:
                joueurX = Math.max(0, joueurX - vitesse);
                break;
            case KeyEvent.VK_RIGHT:
                joueurX = Math.min(770, joueurX + vitesse);
                break;
            case KeyEvent.VK_ESCAPE:
                enCours = false;
                break;
        }
    }
    
    @Override
    public void keyReleased(KeyEvent e) {}
    
    @Override
    public void keyTyped(KeyEvent e) {}
    
    public static void main(String[] args) {
        ExempleJeu jeu = new ExempleJeu();
        jeu.jouer();
    }
}
```

## Dépannage

### Problèmes courants

1. **ClassNotFoundException: mg2d.Fenetre**
   - Vérifiez que MG2D est dans le classpath
   - Confirmez que le fichier .jar est accessible

2. **NoClassDefFoundError**
   - Vérifiez la version de Java (Java 8 recommandé)
   - Assurez-vous que tous les .jar nécessaires sont inclus

3. **Problèmes d'affichage**
   - Vérifiez que le mode plein écran est supporté
   - Testez avec différentes résolutions

### Vérification de l'installation

```bash
# Tester si MG2D est accessible
java -cp lib/mg2d.jar mg2d.Fenetre

# Vérifier le contenu du JAR
jar tf lib/mg2d.jar
```

## Ressources supplémentaires

- **Documentation MG2D** : http://www.iut-calais.info/mg2d/
- **Exemples de projets** : Dépôt GitHub de l'IUT de Calais
- **Support** : Contactez les professeurs de l'IUT de Calais
