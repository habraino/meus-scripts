/**
 * Aula01
 */
public class Aula01 {

    public static void main(String[] args) {
        
        System.out.println("=========  Inicio do Programa =========");

        // implementação da classe anônima Runnable
        Runnable r1 = new Runnable(){
            @Override
            public void run(){
                System.out.println("Estudo da expressão LAMBDA 1.");
            }
        };

        Runnable r2 = () -> System.out.println("Estudo da expressão LAMBDA 2.");

        r1.run();
        r2.run();

    }
}