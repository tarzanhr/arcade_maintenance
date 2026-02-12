# Bouton

**Fichier source:** `Bouton.java`

## Description

Classe représentant un bouton de jeu dans l'interface graphique.  Cette classe modélise un bouton cliquable dans le menu de sélection. Chaque bouton contient le nom du jeu, son chemin d'accès, et les éléments graphiques associés (texte et texture).   @author IUT de Calais @version 1.0 @since 1.0

## Attributs

### `texte` : `Texte`

Classe représentant un bouton de jeu dans l'interface graphique.  Cette classe modélise un bouton cliquable dans le menu de sélection. Chaque bouton contient le nom du jeu, son chemin d'accès, et les éléments graphiques associés (texte et texture).   @author IUT de Calais @version 1.0 @since 1.0 /
public class Bouton {
/  Texte affiché sur le bouton

### `chemin` : `String`

Chemin d'accès au jeu

### `nom` : `String`

Nom du jeu

### `texture` : `Texture`

Texture de fond du bouton

### `numeroDeJeu` : `int`

Numéro identifiant du jeu dans le menu

## Méthodes

### `remplirBouton()`

Classe représentant un bouton de jeu dans l'interface graphique.  Cette classe modélise un bouton cliquable dans le menu de sélection. Chaque bouton contient le nom du jeu, son chemin d'accès, et les éléments graphiques associés (texte et texture).   @author IUT de Calais @version 1.0 @since 1.0 /
public class Bouton {
/  Texte affiché sur le bouton /
private Texte texte;
/  Chemin d'accès au jeu /
private String chemin;
/  Nom du jeu /
private String nom;
/  Texture de fond du bouton /
private Texture texture;
/  Numéro identifiant du jeu dans le menu /
private int numeroDeJeu;
/   Constructeur par défaut.  Initialise un bouton vide avec tous les attributs à null.  /
public Bouton(){
this.texte = null;
this.texture = null;
this.chemin = null;
this.nom = null;
}
/   Constructeur complet de la classe Bouton.  @param texte Le texte à afficher sur le bouton @param texture La texture de fond du bouton @param chemin Le chemin d'accès au jeu @param nom Le nom du jeu /
public Bouton(Texte texte, Texture texture, String chemin, String nom){
this.texte = texte;
this.texture = texture;
this.chemin = chemin;
this.nom = nom;
}
/   Remplit statiquement le tableau de boutons avec les jeux disponibles.  Cette méthode parcourt le répertoire "projet/" pour découvrir tous les jeux et crée un bouton pour chacun. Les boutons sont positionnés verticalement dans le menu avec un espacement de 110 pixels.

### `getChemin()`

Retourne le chemin d'accès au jeu.  @return Le chemin du jeu

### `setChemin()`

Définit le chemin d'accès au jeu.  @param chemin Le nouveau chemin du jeu

### `getNom()`

Retourne le nom du jeu.  @return Le nom du jeu

### `setNom()`

Définit le nom du jeu.  @param nom Le nouveau nom du jeu

### `getTexte()`

Retourne le texte affiché sur le bouton.  @return Le texte du bouton

### `setTexte()`

Définit le texte affiché sur le bouton.  @param texte Le nouveau texte à afficher

### `getTexture()`

Retourne la texture de fond du bouton.  @return La texture du bouton

### `setTexture()`

Définit la texture de fond du bouton.  @param texture La nouvelle texture de fond

### `getNumeroDeJeu()`

Retourne le numéro identifiant du jeu.  @return Le numéro du jeu

### `setNumeroDeJeu()`

Définit le numéro identifiant du jeu.  @param numeroDeJeu Le nouveau numéro du jeu

