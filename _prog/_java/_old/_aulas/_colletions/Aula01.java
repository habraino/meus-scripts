import java.util.List;
import java.util.LinkedList;
import java.util.ListIterator;

/**
 * Aula01
 */
public class Aula01 {

    public static void main(String[] args) {
        
        // lista de cores 1
        String[] colors1 = {"green", "red", "yellow", "brown", "white"};

        List<String> list1 = new LinkedList<>();

        // passa todos os itens para lista1
        for (String colString : colors1) {
            list1.add(colString);
        }

        // lista de cores 2
        String[] colors2 = {"gray", "silver", "blue", "violet", "pink"};

        List<String> list2 = new LinkedList<>();

        // passa todos os itens para lista2
        for(String itens : colors2){
            list2.add(itens);
        }

        list1.addAll(list2);
        list2 = null;
        printList(list1);
        convertToUpperCase(list1);
        printList(list1);

        System.out.printf("\nDeleting elements 4 to 6...\n");
        removeItens(list1, 4, 7);
        printList(list1);
        printReversedList(list1);

    }

    // método para imprimir a lista completa
    private static void printList(List<String> list){
        System.out.printf("%nlist:%n");

        for(String color : list){
            System.out.printf("%s ", color);
        }
        System.out.println();
    }

    // método para mandar todos os elementos para maiúsculas
    private static void convertToUpperCase(List<String> list){
        ListIterator<String>  iterator = list.listIterator();
        while (iterator.hasNext()){
            String color = iterator.next();
            iterator.set(color.toUpperCase());
        }
    }

    // método para remover itens da lista
    private static void removeItens(List<String> list, int start, int end){
        list.subList(start, end).clear();
    }

    // método para reverter a ordem da lista
    private static void printReversedList(List<String> list){
        ListIterator<String> iterator = list.listIterator(list.size());

        System.out.println("\nReversed list:");

        while (iterator.hasPrevious()){
            System.out.printf("%s ", iterator.previous());
        }
        System.out.println();
    }

}