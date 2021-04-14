import java.util.PriorityQueue;

/**
 * Aula08
 */
public class Aula08 {

    public static void main(String[] args) {
        
        /**
         * .offer() → para inserir o elemento 
         * .poll() → para remover o elemento de mais alta prioridade
         * .peek() → para obter uma referência ao elemento de mais alta prioridade
         * .clear() → para remover todos os elementos da fila de prioridade
         * .size() → para obter o número de elementos da fila de prioridade
         */

        PriorityQueue<Double> queue = new PriorityQueue<>();

        // inserindo os elementos
        queue.offer(2.5);
        queue.offer(5.7);
        queue.offer(9.5);

        System.out.print("Polling from queue: ");

        // exibie os elementos da fila
        while(queue.size() > 0) {
            System.out.printf("%.1f ", queue.peek()); // visualiza o elemento superior
            queue.poll(); // remove o elemento superior
        }
        System.out.println();
    }
}