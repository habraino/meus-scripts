
/**
 * Runable
 */
public class Runable {

    public static void main(String[] args) {  
        
        /*Runnable r = new Runnable() {
            public void run(){
                for(int i = 1; i <= 100; i++){
                    System.out.println(i);
                }
            }
        };
        new Thread(r).start();*/

        /*Runnable r = () -> {
            int a = 1;
            while(a <= 10){
                System.out.println(a);
                a++;
            }
        };
        new Thread(r).start();*/

        new Thread(() -> {
            for(int i = 1; i <= 5; i++){
                System.out.println(i);
            }
        }).start();

    }
}