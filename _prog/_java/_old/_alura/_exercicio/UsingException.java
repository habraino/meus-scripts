/**
 * UsingException
 */
public class UsingException {

    public static void main(String[] args) {
        
        try {
            throwExample();
        } catch (Exception e) {
            System.out.println("Exception handled in main.");
        }

    }

    public static void throwExample() throws Exception
    {
        try {
            System.out.println("Method throwExample");
            throw new Exception();

        } catch (RuntimeException rException) {
            System.err.println("Exception handled in throwsException.");
        } finally {
            System.err.println("Finally is always executed.");
        }
        
    }

}