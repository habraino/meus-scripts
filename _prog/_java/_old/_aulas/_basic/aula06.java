/**
 * aula06
 */
public class aula06 {

    public static void main(String[] args) {
        int[] array = {17, 18, 20, 21, 25, 27, 30, 57};

        System.out.printf("%5s%7s\n", "Indice", "Valor");

        for(int i = 0; i < array.length; i++){
            System.out.printf("%4d%7d\n", i, array[i]);
        }
    }
}