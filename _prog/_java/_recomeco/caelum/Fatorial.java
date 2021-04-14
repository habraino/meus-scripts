package caelum;

import java.util.Scanner;

public class Fatorial {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        int fat = 1;
        
        System.out.print("Informe um valor inteiro: ");
        int num = scan.nextInt();
        
        for (int i = 1; i <= num; ++i) {
            fat *= i;
        }

        System.out.printf("!%d = %d%n", num,fat);

        scan.close();
    }

}