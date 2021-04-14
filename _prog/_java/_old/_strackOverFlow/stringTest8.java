/**
 * stringTest8
 */
public class stringTest8 {

    public static void main(String[] args) {
        
        String std = "study";
        std.concat("tonigth");
        System.out.println(std);

        StringBuffer sBuffer = new StringBuffer(std);
        sBuffer.append(" ").append("tonight");
        System.out.println(sBuffer);

        StringBuilder sBuilder = new StringBuilder(std);
        sBuilder.append(" ").append("tonight");
        System.out.println(sBuilder);
    }
}