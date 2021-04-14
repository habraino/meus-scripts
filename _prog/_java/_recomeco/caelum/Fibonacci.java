package caelum;

import java.util.Scanner;

public class Fibonacci {

    public static int fibo(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return fibo(n - 1) + fibo(n - 2);
        }
    }

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);

        System.out.print("Informe um valor inteiro: ");
        int num = scan.nextInt();

        
        System.out.println(fibo(num));

        scan.close();
        

    }

}