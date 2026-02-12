import MG2D.geometrie.Point;
import MG2D.geometrie.Rectangle;
import MG2D.geometrie.Texture;

/**
 * Classe représentant une boîte d'image dans l'interface graphique.
 * <p>
 * Cette classe gère l'affichage d'une image miniature (photo_small.png)
 * pour chaque jeu dans l'interface de sélection.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public class BoiteImage extends Boite{

    /** Texture contenant l'image du jeu */
    Texture image;

    /**
     * Constructeur de la classe BoiteImage.
     * <p>
     * Initialise la boîte avec une image chargée depuis le chemin spécifié.
     * L'image est automatiquement positionnée et dimensionnée.
     * </p>
     * 
     * @param rectangle Le rectangle définissant la position et la taille de la boîte
     * @param image Le chemin du répertoire contenant l'image photo_small.png
     */
    BoiteImage(Rectangle rectangle, String image) {
	super(rectangle);
	this.image = new Texture(image+"/photo_small.png", new Point(760, 648));
    }

    /**
     * Retourne la texture de l'image actuelle.
     * 
     * @return La texture contenant l'image du jeu
     */
    public Texture getImage() {
	return this.image;
    }

    /**
     * Modifie l'image affichée.
     * <p>
     * Change l'image source en chargeant photo_small.png depuis
     * le nouveau chemin spécifié.
     * </p>
     * 
     * @param chemin Le nouveau chemin du répertoire contenant l'image
     */
    public void setImage(String chemin) {
	this.image.setImg(chemin+"/photo_small.png");
    }

}
