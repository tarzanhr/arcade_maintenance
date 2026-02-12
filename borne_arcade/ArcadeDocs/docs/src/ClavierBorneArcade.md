# ClavierBorneArcade

**Fichier source:** `ClavierBorneArcade.java`

## Description

Cette classe implémente les méthodes de KeyListener permettant la gestion du clavier.  Elle permet de gérer le clavier dans des applications développées pour la borne d'arcade de l'IUT.  Les joysticks sont nommés joyJ1 et joyJ2. joyJ1Haut la touche envoyée lorsque le joystick 1 est poussé vers le haut, joyJ1Bas, joyJ1Gauche, joyJ1Droite lorsqu'il est poussé, respectivement, vers le bas, la gauche et la droite.  Les boutons sont nommés boutonJ1 et boutonJ2. Il y a 6 boutons possibles pour chaque joueur. Ils sont notés A, B et C pour les boutons du bas et X, Y et Z pour les boutons du haut. Ils sont donc notés boutonJ1A, boutonJ1B, boutonJ1C, boutonJ1X, boutonJ1Y et boutonJ1Z.  Pour chacune des directions des joysticks ou des boutons, deux méthodes seront présentes : une méthode pour savoir si la direction ou le bouton est pressé ou une autre méthode pour savoir s'il a été pressé.  Elle fonctionne sur le principe de booléen que l'on change quand on appuie ou relâche les touches.  @author IUT de Calais @version 1.0 @since 1.0

## Méthodes

### `getJoyJ1GaucheEnfoncee()`

Cette classe implémente les méthodes de KeyListener permettant la gestion du clavier.  Elle permet de gérer le clavier dans des applications développées pour la borne d'arcade de l'IUT.  Les joysticks sont nommés joyJ1 et joyJ2. joyJ1Haut la touche envoyée lorsque le joystick 1 est poussé vers le haut, joyJ1Bas, joyJ1Gauche, joyJ1Droite lorsqu'il est poussé, respectivement, vers le bas, la gauche et la droite.  Les boutons sont nommés boutonJ1 et boutonJ2. Il y a 6 boutons possibles pour chaque joueur. Ils sont notés A, B et C pour les boutons du bas et X, Y et Z pour les boutons du haut. Ils sont donc notés boutonJ1A, boutonJ1B, boutonJ1C, boutonJ1X, boutonJ1Y et boutonJ1Z.  Pour chacune des directions des joysticks ou des boutons, deux méthodes seront présentes : une méthode pour savoir si la direction ou le bouton est pressé ou une autre méthode pour savoir s'il a été pressé.  Elle fonctionne sur le principe de booléen que l'on change quand on appuie ou relâche les touches.  @author IUT de Calais @version 1.0 @since 1.0 /
public class ClavierBorneArcade implements KeyListener {
// Attributs //
private boolean gauche;
private boolean gaucheTape;
private boolean droite;
private boolean droiteTape;
private boolean haut;
private boolean hautTape;
private boolean bas;
private boolean basTape;
private boolean a;
private boolean aTape;
private boolean z;
private boolean zTape;
private boolean e;
private boolean eTape;
private boolean q;
private boolean qTape;
private boolean s;
private boolean sTape;
private boolean d;
private boolean dTape;
private boolean b;
private boolean bTape;
private boolean k;
private boolean kTape;
private boolean l;
private boolean lTape;
private boolean m;
private boolean mTape;
private boolean o;
private boolean oTape;
private boolean f;
private boolean fTape;
private boolean g;
private boolean gTape;
private boolean h;
private boolean hTape;
private boolean r;
private boolean rTape;
private boolean t;
private boolean tTape;
private boolean y;
private boolean yTape;
// Constructeur //
/   Crée un clavier et initialise tous les attributs à faux pour touches relâchés. /
public ClavierBorneArcade () {
gauche = gaucheTape = droite = droiteTape = false;
haut = hautTape = bas = basTape = false;
a = d = e = k = l = m = o = q = s = z = false;
aTape = dTape = eTape = kTape = lTape = mTape = oTape = qTape = sTape = zTape = false;
f = g = h = r = t = y = false;
fTape = gTape = hTape = rTape = tTape = yTape = false;
}
// Accesseurs //
// Getter //
/   Permet de savoir si la touche "flèche gauche" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "flèche gauche" : vrai pour enfoncée, faux sinon.

### `getJoyJ1GaucheTape()`

Permet de savoir si la touche "flèche gauche" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "flèche gauche tapée" : vrai pour tapée, faux sinon.

### `getJoyJ1DroiteEnfoncee()`

Permet de savoir si la touche "flèche droite" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "flèche droite" : vrai pour enfoncée, faux sinon.

### `getJoyJ1DroiteTape()`

Permet de savoir si la touche "flèche droite" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "flèche droite tapée" : vrai pour tapée, faux sinon.

### `getJoyJ1HautEnfoncee()`

Permet de savoir si la touche "flèche haut" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "flèche haut" : vrai pour enfoncée, faux sinon.

### `getJoyJ1HautTape()`

Permet de savoir si la touche "flèche haut" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "flèche haut tapée" : vrai pour tapée, faux sinon.

### `getJoyJ1BasEnfoncee()`

Permet de savoir si la touche "flèche bas" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "flèche bas" : vrai pour enfoncée, faux sinon.

### `getJoyJ1BasTape()`

Permet de savoir si la touche "flèche bas" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "flèche bas tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ2XEnfoncee()`

Permet de savoir si la touche "a" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "a" : vrai pour enfoncée, faux sinon.

### `getBoutonJ2XTape()`

Permet de savoir si la touche "a" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "a tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ2YEnfoncee()`

Permet de savoir si la touche "z" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "z" : vrai pour enfoncée, faux sinon.

### `getBoutonJ2YTape()`

Permet de savoir si la touche "z" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "z tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ2ZEnfoncee()`

Permet de savoir si la touche "e" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "e" : vrai pour enfoncée, faux sinon.

### `getBoutonJ2ZTape()`

Permet de savoir si la touche "e" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "e tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ2AEnfoncee()`

Permet de savoir si la touche "q" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "q" : vrai pour enfoncée, faux sinon.

### `getBoutonJ2ATape()`

Permet de savoir si la touche "q" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "q tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ2BEnfoncee()`

Permet de savoir si la touche "s" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "s" : vrai pour enfoncée, faux sinon.

### `getBoutonJ2BTape()`

Permet de savoir si la touche "s" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "s tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ2CEnfoncee()`

Permet de savoir si la touche "d" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "d" : vrai pour enfoncée, faux sinon.

### `getBoutonJ2CTape()`

Permet de savoir si la touche "d" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "d tapée" : vrai pour tapée, faux sinon.

### `getJoyJ2GaucheEnfoncee()`

Permet de savoir si la touche "k" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "k" : vrai pour enfoncée, faux sinon.

### `getJoyJ2GaucheTape()`

Permet de savoir si la touche "k" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "k tapée" : vrai pour tapée, faux sinon.

### `getJoyJ2BasEnfoncee()`

Permet de savoir si la touche "l" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "l" : vrai pour enfoncée, faux sinon.

### `getJoyJ2BasTape()`

Permet de savoir si la touche "l" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "l tapée" : vrai pour tapée, faux sinon.

### `getJoyJ2DroiteTape()`

Permet de savoir si la touche "m" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "m tapée" : vrai pour tapée, faux sinon.

### `getJoyJ2DroiteEnfoncee()`

Permet de savoir si la touche "m" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "m" : vrai pour enfoncée, faux sinon.

### `getJoyJ2HautEnfoncee()`

Permet de savoir si la touche "o" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "o" : vrai pour enfoncée, faux sinon.

### `getJoyJ2HautTape()`

Permet de savoir si la touche "o" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "o tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1ATape()`

Permet de savoir si la touche "f" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "f tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1AEnfoncee()`

Permet de savoir si la touche "f" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "f" : vrai pour enfoncée, faux sinon.

### `getBoutonJ1BTape()`

Permet de savoir si la touche "g" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "g tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1BEnfoncee()`

Permet de savoir si la touche "g" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "g" : vrai pour enfoncée, faux sinon.

### `getBoutonJ1CTape()`

Permet de savoir si la touche "h" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "h tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1CEnfoncee()`

Permet de savoir si la touche "h" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "h" : vrai pour enfoncée, faux sinon.

### `getBoutonJ1XTape()`

Permet de savoir si la touche "r" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "r tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1XEnfoncee()`

Permet de savoir si la touche "r" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "r" : vrai pour enfoncée, faux sinon.

### `getBoutonJ1YTape()`

Permet de savoir si la touche "t" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "t tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1YEnfoncee()`

Permet de savoir si la touche "t" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "t" : vrai pour enfoncée, faux sinon.

### `getBoutonJ1ZTape()`

Permet de savoir si la touche "y" a été appuyée puis relâchée. @return retourne la valeur du booléen correspondant à la touche "y tapée" : vrai pour tapée, faux sinon.

### `getBoutonJ1ZEnfoncee()`

Permet de savoir si la touche "y" est enfoncée ou non. @return retourne la valeur du booléen correspondant à la touche "y" : vrai pour enfoncée, faux sinon.

### `reinitialisation()`

Méthode permettant la reinitialisation du clavier. Reinitialisation de tous les événements.

