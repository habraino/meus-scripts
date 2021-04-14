import java.util.Scanner;

/**
 * loop04
 * 
 * calcula o fatorial de um número positivo não nulo
 */
public class loop04 {

    public static void main(String[] args) {
        
        // variáves úteis
        int num = 0;
        int fat = 1;
        int cont = 0;

        Scanner scan = new Scanner(System.in);

        // lê um num e armazena na variável 'num'
        System.out.print("Informe um valor inteiro não nulo: ");
        num = scan.nextInt();
        cont = num;// cont recebe o 'num' informado


        // enquanto cont for maior ou igual à 1
        while(cont >= 1){
            fat *= cont;// calcula o fatorial
            cont--;// tira um valor do cont
        }
        // mostra o resultado na tela
        System.out.printf("%d! = %d\n", num, fat);

    }
}