import MG2D.geometrie.Rectangle;

/**
 * Classe abstraite représentant une boîte générique dans l'interface graphique.
 * <p>
 * Cette classe sert de base pour tous les éléments d'interface qui ont une
 * forme rectangulaire et une position définie.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public abstract class Boite {
    private Rectangle rectangle;
	
    /**
     * Constructeur de la classe Boite.
     * 
     * @param rectangle Le rectangle définissant la position et la taille de la boîte
     */
    Boite(Rectangle rectangle){
	this.rectangle = rectangle;
    }

    /**
     * Retourne le rectangle représentant la boîte.
     * 
     * @return Le rectangle de la boîte
     */
    public Rectangle getRectangle() {
	return rectangle;
    }

    /**
     * Définit le rectangle de la boîte.
     * 
     * @param rectangle Le nouveau rectangle à assigner
     */
    public void setRectangle(Rectangle rectangle) {
	this.rectangle = rectangle;
    }
}
