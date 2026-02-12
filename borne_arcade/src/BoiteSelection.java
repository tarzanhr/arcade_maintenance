import java.awt.Font;
import java.io.IOException;
import java.nio.file.*;
import javax.swing.*;
import java.awt.GraphicsDevice;
import java.awt.GraphicsEnvironment;
import MG2D.geometrie.Rectangle;
import MG2D.Clavier;
import MG2D.audio.*;
import java.io.File;
import MG2D.geometrie.Texte;
import MG2D.Couleur;

/**
 * Classe représentant une boîte de sélection dans l'interface graphique.
 * <p>
 * Cette classe gère la navigation dans le menu de sélection des jeux
 * en utilisant le joystick et les boutons de la borne d'arcade.
 * Elle permet de naviguer verticalement dans la liste des jeux.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public class BoiteSelection extends Boite{
    Pointeur pointeur;
    Font font;

    /**
     * Constructeur de la classe BoiteSelection.
     * 
     * @param rectangle Le rectangle définissant la position et la taille de la boîte
     * @param pointeur Le pointeur utilisé pour la navigation
     */
    public BoiteSelection(Rectangle rectangle, Pointeur pointeur) {
	super(rectangle);
	this.pointeur = pointeur;
    }

    /**
     * Gère la sélection et la navigation dans le menu.
     * <p>
     * Cette méthode gère les entrées du clavier de la borne d'arcade pour
     * naviguer dans la liste des jeux. Elle utilise le joystick pour monter/descendre
     * et le bouton Z pour valider la sélection. La navigation est circulaire.
     * </p>
     * 
     * @param clavier Le clavier de la borne d'arcade
     * @return true si la navigation continue, false si un jeu est sélectionné
     */
    public boolean selection(ClavierBorneArcade clavier){
	// Chargement de la police personnalisée
	font = null;
	try{
	    File in = new File("assets/fonts/PrStart.ttf");
	    font = font.createFont(Font.TRUETYPE_FONT, in);
	    font = font.deriveFont(26.0f);
	}catch (Exception e) {
	    System.out.println("Erreur lors du chargement de la police: " + e.getMessage());
	}
	
	// Bruitage pour la navigation
	Bruitage selection = new Bruitage("assets/sound/bip.mp3");
	
	// Navigation vers le haut (joystick haut)
	if(clavier.getJoyJ1HautTape() &&( pointeur.getValue() <= Graphique.tableau.length - 1)){
		if(Graphique.textesAffiches[pointeur.getValue()]==false){
			Graphique.afficherTexte(pointeur.getValue());
			Graphique.textesAffiches[pointeur.getValue()]=true;
		}
		try{
		    selection.lecture();
		}catch(Exception e){}
		if(pointeur.getValue() == Graphique.tableau.length -1){
			pointeur.setValue(0);
				for(int i = 0 ; i < Graphique.tableau.length ; i++){
					Graphique.tableau[i].getTexte().translater(0, 110*(Graphique.tableau.length -1));
					Graphique.tableau[i].getTexture().translater(0, 110*(Graphique.tableau.length -1));
					Graphique.tableau[i].getTexte().setPolice(font);
					Graphique.tableau[i].getTexte().setCouleur(Couleur.BLANC);
				}
		}else{
			for(int i = 0 ; i < Graphique.tableau.length ; i++){
				Graphique.tableau[i].getTexte().translater(0, -110);
				Graphique.tableau[i].getTexture().translater(0, -110);
				Graphique.tableau[i].getTexte().setPolice(font);
				Graphique.tableau[i].getTexte().setCouleur(Couleur.BLANC);
			}
			pointeur.setValue(pointeur.getValue() + 1);
		}	
	}
	// Navigation vers le bas (joystick bas)
	if(clavier.getJoyJ1BasTape() && pointeur.getValue() >= 0){
		if(Graphique.textesAffiches[pointeur.getValue()]==false){
			Graphique.afficherTexte(pointeur.getValue());
			Graphique.textesAffiches[pointeur.getValue()]=true;
		}
	    try{
			selection.lecture();
		}catch(Exception e){}
		if(pointeur.getValue() == 0){
			pointeur.setValue(Graphique.tableau.length-1);	
			for(int i = 0 ; i < Graphique.tableau.length ; i++){
				Graphique.tableau[i].getTexte().translater(0, -110*(Graphique.tableau.length-1));
				Graphique.tableau[i].getTexture().translater(0, -110*(Graphique.tableau.length-1));
				Graphique.tableau[i].getTexte().setPolice(font);
				Graphique.tableau[i].getTexte().setCouleur(Couleur.BLANC);
					
			}
		}else{
			for(int i = 0 ; i < Graphique.tableau.length ; i++){
				Graphique.tableau[i].getTexte().translater(0, 110);
				Graphique.tableau[i].getTexture().translater(0, 110);
				Graphique.tableau[i].getTexte().setPolice(font);
				Graphique.tableau[i].getTexte().setCouleur(Couleur.BLANC);
					
			}
		
			pointeur.setValue(pointeur.getValue() -1);	
			System.out.println(pointeur.getValue());		
		}
	}
		// Validation de la sélection (bouton Z)
	if(clavier.getBoutonJ1ZTape()){
	    return false;
	}
	return true;
    }

    /**
     * Retourne le pointeur de navigation.
     * 
     * @return Le pointeur actuel
     */
    public Pointeur getPointeur() {
	return pointeur;
    }

    /**
     * Définit le pointeur de navigation.
     * 
     * @param pointeur Le nouveau pointeur à utiliser
     */
    public void setPointeur(Pointeur pointeur) {
	this.pointeur = pointeur;
    }

}
