# Graphique

**Fichier source:** `Graphique.java`

## Description

Classe principale de l'interface graphique de la borne d'arcade.  Cette classe gère l'affichage complet du menu principal, y compris la sélection des jeux, l'affichage des descriptions, des high scores, et la gestion des entrées utilisateur. Elle coordonne tous les éléments visuels et audio de l'interface.   @author IUT de Calais @version 1.0 @since 1.0

## Attributs

### `TAILLEX` : `int`

Classe principale de l'interface graphique de la borne d'arcade.  Cette classe gère l'affichage complet du menu principal, y compris la sélection des jeux, l'affichage des descriptions, des high scores, et la gestion des entrées utilisateur. Elle coordonne tous les éléments visuels et audio de l'interface.   @author IUT de Calais @version 1.0 @since 1.0 /
public class Graphique {
/  Fenêtre principale de l'application en plein écran /
private static final FenetrePleinEcran f = new FenetrePleinEcran("_Menu Borne D'arcade_");
/  Largeur de l'écran

### `TAILLEY` : `int`

Hauteur de l'écran

### `clavier` : `ClavierBorneArcade`

Gestionnaire des entrées de la borne d'arcade

### `bs` : `BoiteSelection`

Boîte de sélection pour naviguer dans le menu

### `pointeur` : `Pointeur`

Tableau statique des boutons de jeux /
public static Bouton[] tableau;
/  Pointeur visuel de sélection

### `musiqueFond` : `Bruitage`

Tableau indiquant quels textes sont affichés /
public static boolean[] textesAffiches;
/  Musique de fond jouée dans le menu

### `cptMus` : `int`

Tableau des musiques disponibles pour le menu /
private static String[] tableauMusiques;
/  Compteur pour la rotation des musiques

## Méthodes

### `selectionJeu()`

Classe principale de l'interface graphique de la borne d'arcade.  Cette classe gère l'affichage complet du menu principal, y compris la sélection des jeux, l'affichage des descriptions, des high scores, et la gestion des entrées utilisateur. Elle coordonne tous les éléments visuels et audio de l'interface.   @author IUT de Calais @version 1.0 @since 1.0 /
public class Graphique {
/  Fenêtre principale de l'application en plein écran /
private static final FenetrePleinEcran f = new FenetrePleinEcran("_Menu Borne D'arcade_");
/  Largeur de l'écran /
private int TAILLEX;
/  Hauteur de l'écran /
private int TAILLEY;
/  Gestionnaire des entrées de la borne d'arcade /
private ClavierBorneArcade clavier;
/  Boîte de sélection pour naviguer dans le menu /
private BoiteSelection bs;
private BoiteImage bi;
private BoiteDescription bd;
/  Tableau statique des boutons de jeux /
public static Bouton[] tableau;
/  Pointeur visuel de sélection /
private Pointeur pointeur;
Font font;
Font fontSelect;
/  Tableau indiquant quels textes sont affichés /
public static boolean[] textesAffiches;
/  Musique de fond jouée dans le menu /
public static Bruitage musiqueFond;
/  Tableau des musiques disponibles pour le menu /
private static String[] tableauMusiques;
/  Compteur pour la rotation des musiques /
private static int cptMus;
/   Constructeur de la classe Graphique.  Initialise tous les composants de l'interface graphique : - Définit les dimensions de l'écran (1280x1024) - Charge les polices personnalisées - Crée les boîtes d'interface - Initialise le tableau de boutons avec les jeux disponibles - Configure le pointeur de sélection - Démarre la musique de fond  /
public Graphique(){
TAILLEX = 1280;
TAILLEY = 1024;
font = null;
try{
File in = new File("assets/fonts/PrStart.ttf");
font = font.createFont(Font.TRUETYPE_FONT, in);
font = font.deriveFont(32.0f);
}catch (Exception e) {
System.err.println(e.getMessage());
}
//f = new Fenetre("_Menu Borne D'arcade_",TAILLEX,TAILLEY);
f.setVisible(true);
clavier = new ClavierBorneArcade();
f.addKeyListener(clavier);
f.getP().addKeyListener(clavier);
/ Retrouver le nombre de jeux dispo /
Path yourPath = FileSystems.getDefault().getPath("projet/");
int cpt=0;
try (DirectoryStream directoryStream = Files.newDirectoryStream(yourPath)) {
for (Path path : directoryStream) {
cpt++;
}
} catch (IOException e) {
e.printStackTrace();
}
tableau = new Bouton[cpt];
textesAffiches = new boolean[cpt];
for(int i=0;i directoryStream = Files.newDirectoryStream(cheminMusiques)) {
for (Path path : directoryStream) {
cptMus++;
}
} catch (IOException e) {
e.printStackTrace();
}
//Creation d'un tableau de musiques
tableauMusiques = new String[cptMus];
try (DirectoryStream directoryStream = Files.newDirectoryStream(cheminMusiques)) {
int i = cptMus-1;
for (Path path : directoryStream) {
tableauMusiques[i]=path.getFileName().toString();
i--;
}
} catch (IOException e) {
e.printStackTrace();
}
//Choix d'une musique aleatoire et lecture de celle-ci
this.lectureMusiqueFond();
}
/   Boucle principale de sélection des jeux.  Gère l'interaction utilisateur dans le menu principal : - Navigation avec le joystick (haut/bas) - Sélection avec le bouton Z - Lancement du jeu avec le bouton A - Menu de confirmation pour quitter - Mise à jour dynamique des descriptions et high scores

### `lectureMusiqueFond()`

Démarre la lecture d'une musique de fond aléatoire.  Choisit une musique au hasard dans le tableau des musiques disponibles et la lance en boucle.

### `stopMusiqueFond()`

Arrête la musique de fond.  Stoppe la lecture en cours de la musique de fond.

### `afficherTexte()`

Affiche le texte d'un jeu spécifique.  Ajoute le texte du bouton de jeu à la fenêtre principale. Utilisé pour afficher dynamiquement les textes lors de la navigation.   @param valeur L'index du jeu dont on veut afficher le texte

