/**
 * Classe représentant une ligne de high score.
 * <p>
 * Cette classe modélise une entrée dans le tableau des high scores,
 * contenant le nom du joueur (limité à 3 caractères) et son score.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
class LigneHighScore{
    /** Nom du joueur (limité à 3 caractères) */
    private String nom;
    /** Score du joueur */
    private int score;

    /**
     * Constructeur par défaut.
     * <p>
     * Initialise une ligne avec "AAA" et un score de 0.
     * </p>
     */
    public LigneHighScore(){
	nom="AAA";
	score=0;
    }

    /**
     * Constructeur avec nom et score.
     * <p>
     * Le nom est automatiquement limité à 3 caractères.
     * Les scores négatifs sont ramenés à 0.
     * </p>
     * 
     * @param nnom Le nom du joueur
     * @param sscore Le score du joueur
     */
    public LigneHighScore(String nnom, int sscore){
	if(nnom.length()>3)
	    nnom="AAA";
	else
	    nom=new String(nnom);
	if(sscore<0)
	    score=0;
	else
	    score=sscore;
    }

    /**
     * Constructeur par copie.
     * 
     * @param l La ligne de high score à copier
     */
    public LigneHighScore(LigneHighScore l){
	nom=new String(l.nom);
	score=l.score;
    }

    /**
     * Constructeur à partir d'une chaîne formatée.
     * <p>
     * La chaîne doit être au format "nom-score".
     * Si le format est incorrect, initialise avec "AAA-0".
     * </p>
     * 
     * @param str La chaîne formatée contenant nom et score
     */
    public LigneHighScore(String str){
	String[] tab = str.split("-");
	if(tab.length!=2){
	    nom = "AAA";
	    score=0;
	}else{
	    nom=new String(tab[0]);
	    score = Integer.parseInt(tab[1]);
	}
	    
    }

    /**
     * Retourne le score du joueur.
     * 
     * @return Le score
     */
    public int getScore(){
	return score;
    }

    /**
     * Retourne le nom du joueur.
     * 
     * @return Le nom (limité à 3 caractères)
     */
    public String getNom(){
	return nom;
    }

    /**
     * Retourne la représentation textuelle de la ligne.
     * <p>
     * Format: "nom-score"
     * </p>
     * 
     * @return La chaîne formatée
     */
    public String toString(){
	return nom+"-"+score;
    }
}
