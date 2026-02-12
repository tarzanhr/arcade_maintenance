import MG2D.*;
import MG2D.geometrie.*;

/**
 * Classe de test pour le système de high scores.
 * <p>
 * Cette classe permet de tester l'interface de saisie de nom
 * pour l'enregistrement des high scores. Elle simule l'ajout
 * d'un score de 40000 points et lance l'interface de saisie.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
class TestHighScore{

    /**
     * Point d'entrée du programme de test des high scores.
     * <p>
     * Crée une fenêtre de test et lance l'interface de saisie
     * de nom avec un score de test de 40000 points.
     * Utilise un fichier de test spécifique pour ne pas affecter
     * les high scores réels des jeux.
     * </p>
     * 
     * @param args Arguments de ligne de commande (non utilisés)
     */
    public static void main(String[] args){
	Fenetre f = new Fenetre("test",1280,1024);
	ClavierBorneArcade clavier = new ClavierBorneArcade();
	f.addKeyListener(clavier);

	HighScore.demanderEnregistrerNom(f,clavier,new Texture("assets/img/shoot.png",new Point(0,0)),40000,"./fichierTestHighScore/text5.hig");
    }
    
}
