import MG2D.geometrie.*;

public class Obstacle extends Texture {

    public Obstacle(Point pointA, Point pointB, String cheminImage) {
        super(cheminImage, pointA, pointB.getX() - pointA.getX(), pointB.getY() - pointA.getY());
    }

    public boolean isOffScreen() {
        return this.getB().getX() < 0;
    }
}
