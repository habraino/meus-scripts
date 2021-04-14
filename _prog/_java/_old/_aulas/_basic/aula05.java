public class aula05 {

    public static void main(String[] args) {
        
        int[] array; // declaração do array
        array = new int[10]; // nova instância do array

        // preenche o array
        for ( int i = 0; i <= 9; i++) {
            System.out.printf("%5d%7d\n",i, array[i]);
        }

    }
}