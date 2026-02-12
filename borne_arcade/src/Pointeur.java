import java.io.IOException;

import MG2D.geometrie.Texture;
import MG2D.Couleur;
import MG2D.geometrie.Point;
import MG2D.geometrie.Triangle;
import MG2D.Clavier;

/**
 * Classe représentant le pointeur de sélection dans le menu.
 * <p>
 * Cette classe gère l'élément visuel qui indique quel jeu est sélectionné
 * dans le menu. Elle contient les textures graphiques (étoiles et rectangle)
 * et gère le lancement du jeu sélectionné.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public class Pointeur {
    /** Valeur numérique du pointeur (index dans le tableau de jeux) */
    private int value;
    /** Texture de l'étoile gauche */
    private Texture triangleGauche;
    /** Texture de l'étoile droite */
    private Texture triangleDroite;
    /** Texture du rectangle de sélection central */
    private Texture rectangleCentre;

    /**
     * Constructeur de la classe Pointeur.
     * <p>
     * Initialise toutes les textures graphiques et positionne le pointeur
     * sur le dernier élément du tableau de jeux.
     * </p>
     */
    public Pointeur(){
	this.triangleGauche = new Texture("assets/img/star.png", new Point(30, 492), 40,40);
	// this.triangleDroite = new Triangle(Couleur .ROUGE, new Point(550, 560), new Point(520, 510), new Point(550, 460), true);
	this.triangleDroite = new Texture("assets/img/star.png", new Point(530, 492), 40,40);
	this.rectangleCentre = new Texture("assets/img/select2.png", new Point(80, 460), 440, 100);
	this.value = Graphique.tableau.length-1;
    }

    /**
     * Lance le jeu sélectionné.
     * <p>
     * Cette méthode est appelée lorsque le bouton A est pressé.
     * Elle arrête la musique de fond, lance le script du jeu sélectionné,
     * attend la fin de l'exécution, puis relance la musique de fond.
     * </p>
     * 
     * @param clavier Le clavier de la borne d'arcade
     */
    public void lancerJeu(ClavierBorneArcade clavier){
	if(clavier.getBoutonJ1ATape()){

	    try {
		Graphique.stopMusiqueFond();
		Process process = Runtime.getRuntime().exec("./projet/"+Graphique.tableau[getValue()].getNom()+"/"+Graphique.tableau[getValue()].getNom()+".sh");
		process.waitFor();		//ajouté afin d'attendre la fin de l'exécution du jeu pour reprendre le contrôle sur le menu
		Graphique.lectureMusiqueFond();
	    } catch (IOException e) {
		e.printStackTrace();
	    } catch(Exception e){	//on catche toutes les exceptions, nécessaire pour le waitFor()
			e.printStackTrace();
	    }
	}
    }

    /**
     * Retourne la valeur numérique du pointeur.
     * <p>
     * Cette méthode permet d'obtenir l'index du jeu sélectionné.
     * </p>
     * 
     * @return L'index du jeu sélectionné
     */
    public int getValue() {
	return value;
    }

    /**
     * Définit la valeur numérique du pointeur.
     * 
     * @param value Le nouvel index du jeu sélectionné
     */
    public void setValue(int value) {
	this.value = value;
    }

    /**
     * Retourne la texture de l'étoile gauche.
     * 
     * @return La texture de l'étoile gauche
     */
    public Texture getTriangleGauche() {
	return triangleGauche;
    }

    /**
     * Définit la texture de l'étoile gauche.
     * 
     * @param triangleGauche La nouvelle texture de l'étoile gauche
     */
    public void setTriangleGauche(Texture triangleGauche) {
	this.triangleGauche = triangleGauche;
    }

    /**
     * Retourne la texture de l'étoile droite.
     * 
     * @return La texture de l'étoile droite
     */
    public Texture getTriangleDroite() {
	return triangleDroite;
    }

    /**
     * Définit la texture de l'étoile droite.
     * 
     * @param triangleDroite La nouvelle texture de l'étoile droite
     */
    public void setTriangleDroite(Texture triangleDroite) {
	this.triangleDroite = triangleDroite;
    }

    /**
     * Retourne la texture du rectangle de sélection.
     * 
     * @return La texture du rectangle central
     */
    public Texture getRectangleCentre() {
	return rectangleCentre;
    }

    /**
     * Définit la texture du rectangle de sélection.
     * 
     * @param rectangleCentre La nouvelle texture du rectangle central
     */
    public void setRectangleCentre(Texture rectangleCentre) {
	this.rectangleCentre = rectangleCentre;
    }

}
