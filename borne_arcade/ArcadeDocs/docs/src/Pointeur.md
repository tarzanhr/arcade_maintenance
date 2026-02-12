# Pointeur

**Fichier source:** `Pointeur.java`

## Description

Classe représentant le pointeur de sélection dans le menu.  Cette classe gère l'élément visuel qui indique quel jeu est sélectionné dans le menu. Elle contient les textures graphiques (étoiles et rectangle) et gère le lancement du jeu sélectionné.   @author IUT de Calais @version 1.0 @since 1.0

## Attributs

### `value` : `int`

Classe représentant le pointeur de sélection dans le menu.  Cette classe gère l'élément visuel qui indique quel jeu est sélectionné dans le menu. Elle contient les textures graphiques (étoiles et rectangle) et gère le lancement du jeu sélectionné.   @author IUT de Calais @version 1.0 @since 1.0 /
public class Pointeur {
/  Valeur numérique du pointeur (index dans le tableau de jeux)

### `triangleGauche` : `Texture`

Texture de l'étoile gauche

### `triangleDroite` : `Texture`

Texture de l'étoile droite

### `rectangleCentre` : `Texture`

Texture du rectangle de sélection central

## Méthodes

### `lancerJeu()`

Classe représentant le pointeur de sélection dans le menu.  Cette classe gère l'élément visuel qui indique quel jeu est sélectionné dans le menu. Elle contient les textures graphiques (étoiles et rectangle) et gère le lancement du jeu sélectionné.   @author IUT de Calais @version 1.0 @since 1.0 /
public class Pointeur {
/  Valeur numérique du pointeur (index dans le tableau de jeux) /
private int value;
/  Texture de l'étoile gauche /
private Texture triangleGauche;
/  Texture de l'étoile droite /
private Texture triangleDroite;
/  Texture du rectangle de sélection central /
private Texture rectangleCentre;
/   Constructeur de la classe Pointeur.  Initialise toutes les textures graphiques et positionne le pointeur sur le dernier élément du tableau de jeux.  /
public Pointeur(){
this.triangleGauche = new Texture("assets/img/star.png", new Point(30, 492), 40,40);
// this.triangleDroite = new Triangle(Couleur .ROUGE, new Point(550, 560), new Point(520, 510), new Point(550, 460), true);
this.triangleDroite = new Texture("assets/img/star.png", new Point(530, 492), 40,40);
this.rectangleCentre = new Texture("assets/img/select2.png", new Point(80, 460), 440, 100);
this.value = Graphique.tableau.length-1;
}
/   Lance le jeu sélectionné.  Cette méthode est appelée lorsque le bouton A est pressé. Elle arrête la musique de fond, lance le script du jeu sélectionné, attend la fin de l'exécution, puis relance la musique de fond.   @param clavier Le clavier de la borne d'arcade

### `getValue()`

Retourne la valeur numérique du pointeur.  Cette méthode permet d'obtenir l'index du jeu sélectionné.   @return L'index du jeu sélectionné

### `setValue()`

Définit la valeur numérique du pointeur.  @param value Le nouvel index du jeu sélectionné

### `getTriangleGauche()`

Retourne la texture de l'étoile gauche.  @return La texture de l'étoile gauche

### `setTriangleGauche()`

Définit la texture de l'étoile gauche.  @param triangleGauche La nouvelle texture de l'étoile gauche

### `getTriangleDroite()`

Retourne la texture de l'étoile droite.  @return La texture de l'étoile droite

### `setTriangleDroite()`

Définit la texture de l'étoile droite.  @param triangleDroite La nouvelle texture de l'étoile droite

### `getRectangleCentre()`

Retourne la texture du rectangle de sélection.  @return La texture du rectangle central

### `setRectangleCentre()`

Définit la texture du rectangle de sélection.  @param rectangleCentre La nouvelle texture du rectangle central

