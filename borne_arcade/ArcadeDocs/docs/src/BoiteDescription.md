# BoiteDescription

**Fichier source:** `BoiteDescription.java`

## Description

Classe représentant une boîte de description dans l'interface graphique.  Cette classe gère l'affichage des descriptions de jeux, les contrôles, et les high scores. Elle étend la classe Boite pour bénéficier de la gestion rectangulaire de base.   @author IUT de Calais @version 1.0 @since 1.0

## Méthodes

### `lireFichier()`

Classe représentant une boîte de description dans l'interface graphique.  Cette classe gère l'affichage des descriptions de jeux, les contrôles, et les high scores. Elle étend la classe Boite pour bénéficier de la gestion rectangulaire de base.   @author IUT de Calais @version 1.0 @since 1.0 /
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
/   Constructeur de la classe BoiteDescription.  Initialise tous les éléments graphiques nécessaires à l'affichage de la description, des contrôles et des high scores.   @param rectangle Le rectangle définissant la position et la taille de la boîte /
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
for(int i = 0 ; i  Lit le fichier description.txt ligne par ligne et affiche jusqu'à 10 lignes dans la boîte de description.   @param path Le chemin du répertoire contenant le fichier description.txt

### `lireHighScore()`

Lit et affiche les high scores depuis un fichier.  Charge les high scores depuis le fichier highscore et les affiche dans un format classé (1er, 2eme, etc.). Si le fichier n'existe pas, affiche des scores vides.   @param path Le chemin du répertoire contenant le fichier highscore

### `lireBouton()`

Lit la configuration des boutons depuis un fichier.  Charge le fichier bouton.txt qui contient les descriptions des contrôles séparées par des deux-points.   @param path Le chemin du répertoire contenant le fichier bouton.txt

### `setMessage()`

Retourne le tableau des messages de description.  @return Le tableau de Texte contenant les messages /
public Texte[] getMessage(){
return message;
}
/   Définit le texte d'un message à une position spécifique.  @param message Le nouveau message à afficher @param a L'index dans le tableau de messages

### `getJoystick()`

Retourne le tableau des textures des boutons.  @return Le tableau de Texture des boutons /
public Texture[] getBouton(){
return this.bouton;
}
/   Retourne la texture du joystick.  @return La texture du joystick

### `gettJoystick()`

Retourne le tableau des textes des boutons.  @return Le tableau de Texte des boutons /
public Texte[] gettBouton(){
return this.tBouton;
}
/   Retourne le texte du joystick.  @return Le Texte associé au joystick

### `getHighscore()`

Retourne le texte d'en-tête "HIGHSCORE".  @return Le Texte "HIGHSCORE"

### `settJoystick()`

Retourne le tableau des high scores affichés.  @return Le tableau de Texte contenant les high scores /
public Texte[] getListeHighScore(){
return this.listeHighScore;
}
/   Définit le texte du joystick.  @param s Le nouveau texte à afficher pour le joystick

### `settBouton()`

Définit le texte d'un bouton spécifique.  @param s Le nouveau texte à afficher @param a L'index du bouton dans le tableau

