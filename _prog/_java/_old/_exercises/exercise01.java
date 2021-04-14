import java.util.Arrays;
import java.util.Scanner;

/**
 * exercise01
 */
public class exercise01 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);

        float media = 0;
        int somaAll = 0, mult = 0;

        int[] array = new int[7];
        int num = 0;

        for(int i = 0; i < array.length; i++){
            System.out.printf("Informe o %dº valor: ",i+1);
            num = scan.nextInt();
            array[i] = num;
            somaAll += array[i];
        }

        /* fecha a classe Scanner */
        scan.close();
    
        media = (float) somaAll / array.length;// calcula a media

        // imprime os resultados
        System.out.println('\n'+Arrays.toString(array));
        System.out.println("Soma total: "+somaAll);
        System.out.printf("Média aritmétrica: %f\n",media);

        // faz leitura do array, para multiplicar o elemento pelo seu índice
        for(int x = 0; x < 7; x++){
            mult = x * array[x];
            System.out.printf("Multiplicação por elem. %d * %d = %d\n",array[x], x, mult);
        }

    }
}