import java.awt.Font;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.File;
import java.util.ArrayList;
import java.io.InputStream;
import java.io.InputStreamReader;
import MG2D.geometrie.Texture;
import MG2D.Couleur;
import MG2D.geometrie.Point;
import MG2D.geometrie.Rectangle;
import MG2D.geometrie.Texte;
import java.io.IOException;

/**
 * Classe représentant une boîte de description dans l'interface graphique.
 * <p>
 * Cette classe gère l'affichage des descriptions de jeux, les contrôles,
 * et les high scores. Elle étend la classe Boite pour bénéficier de la
 * gestion rectangulaire de base.
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public class BoiteDescription extends Boite{

    private Texte[] message;
    private boolean stop;
    private int nombreLigne;
    private Texture joystick;
    private Texture[] bouton;
    private Texte tJoystick;
    private Texte[] tBouton;
    private String[] texteBouton;
    private Texte highscore;
    private Texte[] listeHighScore;
	
	private Font font1 = null;
	private Font font2 = null;
	private Font font3 = null;
	private Font font4 = null;
	
	
	
    /**
     * Constructeur de la classe BoiteDescription.
     * <p>
     * Initialise tous les éléments graphiques nécessaires à l'affichage
     * de la description, des contrôles et des high scores.
     * </p>
     * 
     * @param rectangle Le rectangle définissant la position et la taille de la boîte
     */
    BoiteDescription(Rectangle rectangle) {
	super(rectangle);
	
	// Chargement des polices personnalisées
	try{
	    Font font = null;
		Font fontTexte = null;
		File in = new File("assets/fonts/PrStart.ttf");
		font = font.createFont(Font.TRUETYPE_FONT, in);
		 in = new File("assets/fonts/Volter__28Goldfish_29.ttf");
		fontTexte = fontTexte.createFont(Font.TRUETYPE_FONT, in);
	    font1 = fontTexte.deriveFont(15.0f);
		font2 = fontTexte.deriveFont(20.0f);
		font3 = font.deriveFont(25.0f);
		font4 = font.deriveFont(14.0f);
	}catch (Exception e) {
	    System.err.println("Erreur lors du chargement des polices: " + e.getMessage());
	}
	
	bouton = new Texture[6];
	tBouton = new Texte[6];
	texteBouton = new String[7];
		
	//declaration des texture bouton + joystick
	this.joystick = new Texture("assets/img/joystick2.png", new Point(740, 100), 40,40);
	for(int i = 0 ; i < 3 ; i++){
	    this.bouton[i] = new Texture("assets/img/ibouton2.png", new Point(890+130*i, 130), 40, 40);
	}
	for(int i = 3 ; i < 6 ; i++){
	    this.bouton[i] = new Texture("assets/img/ibouton2.png", new Point(890+130*(i-3), 50), 40, 40);
	}
	
	//declaration des textes bouton + joystick
	this.tJoystick = new Texte(Couleur .NOIR, "...", font1, new Point(760, 80));
	for(int i = 0 ; i < 3 ; i++){
	    this.tBouton[i] = new Texte(Couleur .NOIR, "...", font1, new Point(910+130*i, 120));
	}
	for(int i = 3 ; i < 6 ; i++){
	    this.tBouton[i] = new Texte(Couleur .NOIR, "...", font1, new Point(910+130*(i-3), 40));
	}
	stop = false;
	message = new Texte[10];
	for(int i = 0 ; i < message.length ; i++){
	    message[i] = new Texte(Couleur .NOIR, "", font2, new Point(960, 590));
	    message[i].translater(0, -i*30);

	}
	nombreLigne = 0;

	highscore = new Texte(Couleur.NOIR, "HIGHSCORE", font3, new Point(960, 335));
	listeHighScore = new Texte[10];
	for(int i=0;i<5;i++){
	    listeHighScore[i] = new Texte(Couleur.NOIR, "", font4, new Point(820,310));
	    listeHighScore[i].translater(0,-i*25);
	}
	for(int i=5;i<10;i++){
	    listeHighScore[i] = new Texte(Couleur.NOIR, "", font4, new Point(1100,310));
	    listeHighScore[i].translater(0,-(i-5)*25);
	}
	
	
	/*
	//declaration des textes bouton + joystick
	this.tJoystick = new Texte(Couleur .NOIR, "...", new Font("Calibri", Font.TYPE1_FONT, 15), new Point(760, 80));
	for(int i = 0 ; i < 3 ; i++){
	    this.tBouton[i] = new Texte(Couleur .NOIR, "...", new Font("Calibri", Font.TYPE1_FONT, 15), new Point(910+130*i, 120));
	}
	for(int i = 3 ; i < 6 ; i++){
	    this.tBouton[i] = new Texte(Couleur .NOIR, "...", new Font("Calibri", Font.TYPE1_FONT, 15), new Point(910+130*(i-3), 40));
	}
	stop = false;
	message = new Texte[10];
	for(int i = 0 ; i < message.length ; i++){
	    message[i] = new Texte(Couleur .NOIR, "", new Font("Calibri", Font.TYPE1_FONT, 20), new Point(960, 590));
	    message[i].translater(0, -i*30);

	}
	nombreLigne = 0;

	highscore = new Texte(Couleur.NOIR, "HIGHSCORE", new Font("Calibri", Font.TYPE1_FONT, 25), new Point(960, 335));
	listeHighScore = new Texte[10];
	for(int i=0;i<5;i++){
	    listeHighScore[i] = new Texte(Couleur.NOIR, "", new Font("Calibri", Font.TYPE1_FONT, 17), new Point(820,310));
	    listeHighScore[i].translater(0,-i*25);
	}
	for(int i=5;i<10;i++){
	    listeHighScore[i] = new Texte(Couleur.NOIR, "", new Font("Calibri", Font.TYPE1_FONT, 17), new Point(1100,310));
	    listeHighScore[i].translater(0,-(i-5)*25);
	}*/

    }
	
    /**
     * Lit le fichier de description et met à jour l'affichage.
     * <p>
     * Lit le fichier description.txt ligne par ligne et affiche
     * jusqu'à 10 lignes dans la boîte de description.
     * </p>
     * 
     * @param path Le chemin du répertoire contenant le fichier description.txt
     */
    public void lireFichier(String path){
	//System.out.println(path);
	String fichier =path+"/description.txt";
		
	//lecture du fichier texte	
	try{
	    InputStream ips=new FileInputStream(fichier); 
	    InputStreamReader ipsr=new InputStreamReader(ips);
	    BufferedReader br=new BufferedReader(ipsr);
	    String ligne;
	    while (/*(ligne=br.readLine())!=null &&*/stop == false){
		ligne=br.readLine();
		//System.out.println(ligne);
		if(ligne != null){
		    //changer message
					
		    message[nombreLigne].setTexte(ligne);
		    setMessage(ligne, nombreLigne);
		}else{
		    //changer message
					
		    message[nombreLigne].setTexte("");
		    setMessage("", nombreLigne);
		}
		nombreLigne++;
		if(nombreLigne >= 10){
		    stop = true;
		    nombreLigne = 0;
		}
	    }
	    stop = false;
	    br.close(); 
	}		
	catch (Exception e){
	    System.err.println(e.toString());
	}
    }

	/**
	 * Lit et affiche les high scores depuis un fichier.
	 * <p>
	 * Charge les high scores depuis le fichier highscore et les affiche
	 * dans un format classé (1er, 2eme, etc.). Si le fichier n'existe pas,
	 * affiche des scores vides.
	 * </p>
	 * 
	 * @param path Le chemin du répertoire contenant le fichier highscore
	 */
	public void lireHighScore(String path){
		
		for(int i=0;i<10;i++){
			if(i==0)
				listeHighScore[i].setTexte("1er - ");
			else
				listeHighScore[i].setTexte((i+1)+"eme - ");
		}
		
		String fichier =path+"/highscore";
		
		File f = new File(fichier);
		if(!f.exists()){
			for(int i=0;i<10;i++)
				listeHighScore[i].setTexte("/");
		}else{
			ArrayList<LigneHighScore> liste = HighScore.lireFichier(fichier);
			for(int i=0;i<liste.size();i++){
				if(i==0)
					listeHighScore[i].setTexte("1er : "+liste.get(i).getNom()+" - "+liste.get(i).getScore());
				else
					listeHighScore[i].setTexte((i+1)+"eme : "+liste.get(i).getNom()+" -  "+liste.get(i).getScore());
			}
		}
	}

	/**
	 * Lit la configuration des boutons depuis un fichier.
	 * <p>
	 * Charge le fichier bouton.txt qui contient les descriptions
	 * des contrôles séparées par des deux-points.
	 * </p>
	 * 
	 * @param path Le chemin du répertoire contenant le fichier bouton.txt
	 */
	public void lireBouton(String path){
		//System.out.println(path);
		String fichier =path+"/bouton.txt";
			
		//lecture du fichier texte    
		try{
			InputStream ips=new FileInputStream(fichier); 
			InputStreamReader ipsr=new InputStreamReader(ips);
			BufferedReader br=new BufferedReader(ipsr);
			String ligne;
			ligne = br.readLine();
			if(ligne == null){
				System.err.println("le fichier bouton est surement vide :" + fichier);
			}else{
				texteBouton = ligne.split(":");
				//changer le texte des boutons
				settJoystick(texteBouton[0]);
				for(int i = 0 ; i < 6 ; i++){
					settBouton(texteBouton[i+1], i);
				}                
			}
		}catch(Exception e){System.err.println(e);};
			
	}

	/**
	 * Retourne le tableau des messages de description.
	 * 
	 * @return Le tableau de Texte contenant les messages
	 */
	public Texte[] getMessage(){
		return message;
	}

	/**
	 * Définit le texte d'un message à une position spécifique.
	 * 
	 * @param message Le nouveau message à afficher
	 * @param a L'index dans le tableau de messages
	 */
	public void setMessage(String message, int a) {
		this.message[a].setTexte(message);    
	}

	/**
	 * Retourne le tableau des textures des boutons.
	 * 
	 * @return Le tableau de Texture des boutons
	 */
	public Texture[] getBouton(){
		return this.bouton;
	}

	/**
	 * Retourne la texture du joystick.
	 * 
	 * @return La texture du joystick
	 */
	public Texture getJoystick(){
		return this.joystick;
	}

	/**
	 * Retourne le tableau des textes des boutons.
	 * 
	 * @return Le tableau de Texte des boutons
	 */
	public Texte[] gettBouton(){
		return this.tBouton;
	}

	/**
	 * Retourne le texte du joystick.
	 * 
	 * @return Le Texte associé au joystick
	 */
	public Texte gettJoystick(){
		return this.tJoystick;
	}

	/**
	 * Retourne le texte d'en-tête "HIGHSCORE".
	 * 
	 * @return Le Texte "HIGHSCORE"
	 */
	public Texte getHighscore(){
		return this.highscore;
	}

	/**
	 * Retourne le tableau des high scores affichés.
	 * 
	 * @return Le tableau de Texte contenant les high scores
	 */
	public Texte[] getListeHighScore(){
		return this.listeHighScore;
	}

	/**
	 * Définit le texte du joystick.
	 * 
	 * @param s Le nouveau texte à afficher pour le joystick
	 */
	public void settJoystick(String s){
		this.tJoystick.setTexte(s);        
	}

	/**
	 * Définit le texte d'un bouton spécifique.
	 * 
	 * @param s Le nouveau texte à afficher
	 * @param a L'index du bouton dans le tableau
	 */
	public void settBouton(String s, int a){
		this.tBouton[a].setTexte(s);        
	}
}