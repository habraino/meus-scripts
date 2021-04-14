/**
 * Retangulo
 */

/**
 * Area
 */
class Area {

    public int width, height;

    public int areaTriangulo(){
        return width * height;
    }

    public boolean isBox(){
        if(width == height)
            return true;
        return false;
    }
    
}

public class Retangulo {

    public static void main(String[] args) {
        
        Area a = new Area();
        a.width = 100;
        a.height = 120;
        int b = a.areaTriangulo();

        System.out.println(b);
        System.out.println(a.isBox());

        // ---------------------------
        Area a2 = new Area();
        a2.height = 100;
        a2.width = 100;

        System.out.println(a2.areaTriangulo());
        System.out.println(a2.isBox());

    }
}