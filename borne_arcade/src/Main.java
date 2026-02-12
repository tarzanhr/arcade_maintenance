/**
 * Classe principale de l'application Borne Arcade.
 * <p>
 * Cette classe contient le point d'entrée de l'application et initialise
 * l'interface graphique principale. Elle lance la boucle de sélection
 * des jeux dans un cycle infini.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public class Main {
    /**
     * Point d'entrée principal de l'application.
     * <p>
     * Crée une instance de Graphique et lance la boucle de sélection
     * des jeux. La boucle tourne indéfiniment pour permettre une
     * utilisation continue de la borne d'arcade.
     * </p>
     * 
     * @param args Arguments de ligne de commande (non utilisés)
     */
    public static void main(String[] args){
	Graphique g = new Graphique();
	while(true){
	    try{
		// Thread.sleep(250);
	    }catch(Exception e){};
	    g.selectionJeu();
	}
    }
}
