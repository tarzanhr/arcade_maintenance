# BoiteImage

**Fichier source:** `BoiteImage.java`

## Description

Classe représentant une boîte d'image dans l'interface graphique.  Cette classe gère l'affichage d'une image miniature (photo_small.png) pour chaque jeu dans l'interface de sélection.   @author IUT de Calais @version 1.0 @since 1.0

## Méthodes

### `getImage()`

Classe représentant une boîte d'image dans l'interface graphique.  Cette classe gère l'affichage d'une image miniature (photo_small.png) pour chaque jeu dans l'interface de sélection.   @author IUT de Calais @version 1.0 @since 1.0 /
public class BoiteImage extends Boite{
/  Texture contenant l'image du jeu /
Texture image;
/   Constructeur de la classe BoiteImage.  Initialise la boîte avec une image chargée depuis le chemin spécifié. L'image est automatiquement positionnée et dimensionnée.   @param rectangle Le rectangle définissant la position et la taille de la boîte @param image Le chemin du répertoire contenant l'image photo_small.png /
BoiteImage(Rectangle rectangle, String image) {
super(rectangle);
this.image = new Texture(image+"/photo_small.png", new Point(760, 648));
}
/   Retourne la texture de l'image actuelle.  @return La texture contenant l'image du jeu

### `setImage()`

Modifie l'image affichée.  Change l'image source en chargeant photo_small.png depuis le nouveau chemin spécifié.   @param chemin Le nouveau chemin du répertoire contenant l'image

