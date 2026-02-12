# BoiteSelection

**Fichier source:** `BoiteSelection.java`

## Description

Classe représentant une boîte de sélection dans l'interface graphique.  Cette classe gère la navigation dans le menu de sélection des jeux en utilisant le joystick et les boutons de la borne d'arcade. Elle permet de naviguer verticalement dans la liste des jeux.   @author IUT de Calais @version 1.0 @since 1.0

## Méthodes

### `selection()`

Classe représentant une boîte de sélection dans l'interface graphique.  Cette classe gère la navigation dans le menu de sélection des jeux en utilisant le joystick et les boutons de la borne d'arcade. Elle permet de naviguer verticalement dans la liste des jeux.   @author IUT de Calais @version 1.0 @since 1.0 /
public class BoiteSelection extends Boite{
Pointeur pointeur;
Font font;
/   Constructeur de la classe BoiteSelection.  @param rectangle Le rectangle définissant la position et la taille de la boîte @param pointeur Le pointeur utilisé pour la navigation /
public BoiteSelection(Rectangle rectangle, Pointeur pointeur) {
super(rectangle);
this.pointeur = pointeur;
}
/   Gère la sélection et la navigation dans le menu.  Cette méthode gère les entrées du clavier de la borne d'arcade pour naviguer dans la liste des jeux. Elle utilise le joystick pour monter/descendre et le bouton Z pour valider la sélection. La navigation est circulaire.   @param clavier Le clavier de la borne d'arcade @return true si la navigation continue, false si un jeu est sélectionné

### `getPointeur()`

Retourne le pointeur de navigation.  @return Le pointeur actuel

### `setPointeur()`

Définit le pointeur de navigation.  @param pointeur Le nouveau pointeur à utiliser

