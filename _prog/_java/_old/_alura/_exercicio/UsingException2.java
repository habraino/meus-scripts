/**
 * UsingException2
 */
public class UsingException2 { 

    public static void main(String[] args) {
    
        try {
            function1();
        } catch (Exception e) {
            System.err.printf("%s\n\n", e.getMessage());
            e.printStackTrace();

            StackTraceElement[] sElement = e.getStackTrace();

            System.out.println("\033[1;33mStack trace from getStackTrace.\033[m");
            System.out.println("Class\t\tFile\t\t\tLine\t\tMethod\n");
            for (StackTraceElement sElement2 : sElement) {
                System.out.printf("%s\t", sElement2.getClassName());
                System.out.printf("%s\t", sElement2.getFileName());
                System.out.printf("%s\t", sElement2.getLineNumber());
                System.out.printf("%s\t\n\n", sElement2.getMethodName());
            }
        }
    }

    public static void function1() throws Exception {
        function2();
    }

    public static void function2() throws Exception {
        function3();
    }

    public static void function3() throws Exception {
        throw new Exception("\033[1;36mException throw in function3.\033[m");
    }
}