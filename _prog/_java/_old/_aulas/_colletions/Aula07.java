import java.util.Stack;
import java.util.EmptyStackException;

/**
 * Aula07
 */
public class Aula07 {

    public static void main(String[] args) {
        
        Stack<Number> stack = new Stack<>();

        /**
         * push() -> para adicionar elemento
         * pop() -> para remover elemento
         * 
         * 'Number' pertence a super classe java.lang, ela recebe qualquer tipo    primitvo.
         */

        stack.push(12L);
        System.out.println("Pushed: 12L");
        printStack(stack);
        stack.push(30);
        System.out.println("Pushed: 20");
        printStack(stack);
        stack.push(1.0F);
        System.out.println("Pushed: 1.0F");
        printStack(stack);
        stack.push(2345.345);
        System.out.println("Pushed: 2345.345");
        printStack(stack);
        
        // remove itens da pilha
        try {
            Number remove = null;

            // remove elementos da pilha
            while (true) {
                remove = stack.pop();
                System.out.println("Popped: "+remove);
                printStack(stack);
            }
            
        } catch (EmptyStackException e) {
            System.out.println(stack.isEmpty() == true ? "\033[1;31mDon't have stack\033[m" : "\033[1;31mHave stack\033[m");
        }

    }

    // método para imprimir stack
    private static void printStack(Stack<Number> stack) {
        if(stack.isEmpty()){
            System.out.println("Stack isEmpty!"); // stack vazia
        } else {
            System.out.println("stack contains: "+stack); // stack cheia
        }
    }
}

