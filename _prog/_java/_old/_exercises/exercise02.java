import java.util.Scanner;

/**
 * exercise02
 */
public class exercise02 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);
        float media = 0;
        int soma = 0;
        int num = 0;

        int[] array = new int[5];

        for(int i = 0; i < array.length; i++){
            System.out.printf("Informe %dÂª nota: ", i+1);
            num = scan.nextInt();

            array[i] = num;
            soma += num;
        }

        /* fecha a classe Scanner */
        scan.close();

        media = (float) soma / array.length;

        System.out.println("Soma: "+soma);
        System.out.println("Média: "+media);


    }
}