import java.awt.Font;
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.File;

import MG2D.Couleur;
import MG2D.geometrie.Point;
import MG2D.geometrie.Texture;
import MG2D.geometrie.Texte;

/**
 * Classe représentant un bouton de jeu dans l'interface graphique.
 * <p>
 * Cette classe modélise un bouton cliquable dans le menu de sélection.
 * Chaque bouton contient le nom du jeu, son chemin d'accès, et les éléments
 * graphiques associés (texte et texture).
 * </p>
 * 
 * @author IUT de Calais
 * @version 1.0
 * @since 1.0
 */
public class Bouton {
    /** Texte affiché sur le bouton */
    private Texte texte;
    /** Chemin d'accès au jeu */
    private String chemin;
    /** Nom du jeu */
    private String nom;
    /** Texture de fond du bouton */
    private Texture texture;
    /** Numéro identifiant du jeu dans le menu */
    private int numeroDeJeu;

    /**
     * Constructeur par défaut.
     * <p>
     * Initialise un bouton vide avec tous les attributs à null.
     * </p>
     */
    public Bouton(){
	this.texte = null;
	this.texture = null;
	this.chemin = null;
	this.nom = null;
    }

    /**
     * Constructeur complet de la classe Bouton.
     * 
     * @param texte Le texte à afficher sur le bouton
     * @param texture La texture de fond du bouton
     * @param chemin Le chemin d'accès au jeu
     * @param nom Le nom du jeu
     */
    public Bouton(Texte texte, Texture texture, String chemin, String nom){
	this.texte = texte;
	this.texture = texture;
	this.chemin = chemin;
	this.nom = nom;
    }

    /**
     * Remplit statiquement le tableau de boutons avec les jeux disponibles.
     * <p>
     * Cette méthode parcourt le répertoire "projet/" pour découvrir tous les jeux
     * et crée un bouton pour chacun. Les boutons sont positionnés verticalement
     * dans le menu avec un espacement de 110 pixels.
     * </p>
     */
    public static void remplirBouton(){
	for(int i = 0 ; i < Graphique.tableau.length ; i++){
	    Graphique.tableau[i] = new Bouton();
	}

	Path yourPath = FileSystems.getDefault().getPath("projet/");

	try (DirectoryStream<Path> directoryStream = Files.newDirectoryStream(yourPath)) {
	    int i = Graphique.tableau.length - 1;
	    for (Path path : directoryStream) {
		Graphique.tableau[i].setTexte(new Texte(Couleur .NOIR, path.getFileName().toString(), new Font("Calibri", Font.TYPE1_FONT, 30), new Point(310, 510)));
		Graphique.tableau[i].setTexture(new Texture("assets/img/bouton2.png", new Point(100, 478), 400, 65));
		for(int j=0;j<Graphique.tableau.length-(i+1);j++){
		    Graphique.tableau[i].getTexte().translater(0,-110);
		    Graphique.tableau[i].getTexture().translater(0,-110);
		}
		Graphique.tableau[i].setChemin("projet/"+path.getFileName().toString());
		Graphique.tableau[i].setNom(path.getFileName().toString());
		Graphique.tableau[i].setNumeroDeJeu(i);
		i--;
	    }
	} catch (IOException e) {
	    e.printStackTrace();
	}

    }

    /**
     * Retourne le chemin d'accès au jeu.
     * 
     * @return Le chemin du jeu
     */
    public String getChemin() {
	return chemin;
    }

    /**
     * Définit le chemin d'accès au jeu.
     * 
     * @param chemin Le nouveau chemin du jeu
     */
    public void setChemin(String chemin) {
	this.chemin = chemin;
    }

    /**
     * Retourne le nom du jeu.
     * 
     * @return Le nom du jeu
     */
    public String getNom() {
	return nom;
    }

    /**
     * Définit le nom du jeu.
     * 
     * @param nom Le nouveau nom du jeu
     */
    public void setNom(String nom) {
	this.nom = nom;
    }

    /**
     * Retourne le texte affiché sur le bouton.
     * 
     * @return Le texte du bouton
     */
    public Texte getTexte() {
	return texte;
    }

    /**
     * Définit le texte affiché sur le bouton.
     * 
     * @param texte Le nouveau texte à afficher
     */
    public void setTexte(Texte texte) {
	this.texte = texte;
    }

    /**
     * Retourne la texture de fond du bouton.
     * 
     * @return La texture du bouton
     */
    public Texture getTexture() {
	return texture;
    }

    /**
     * Définit la texture de fond du bouton.
     * 
     * @param texture La nouvelle texture de fond
     */
    public void setTexture(Texture texture) {
	this.texture = texture;
    }

    /**
     * Retourne le numéro identifiant du jeu.
     * 
     * @return Le numéro du jeu
     */
    public int getNumeroDeJeu() {
	return numeroDeJeu;
    }

    /**
     * Définit le numéro identifiant du jeu.
     * 
     * @param numeroDeJeu Le nouveau numéro du jeu
     */
    public void setNumeroDeJeu(int numeroDeJeu) {
	this.numeroDeJeu = numeroDeJeu;
    }
}
