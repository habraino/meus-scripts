import java.util.List;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.Collections;

/**
 * Aula05
 */
public class Aula05 {

    private static enum City {Neves, Londres, Lisboa, Guadalupe};

    public static void main(String[] args) {
    
        List<Enum> list = new LinkedList<>(Arrays.asList(City.values()));
        
        Collections.reverse(list);

        for(Enum e : list){
            System.out.println(e);
        }

        String[] nome = {
            "Joana", "Aida", "Aida", "Sonilza", "Gesiney", "Monica",
            "Silvânia", "Tomazia"
        };

        List<String> list2 = new LinkedList<>(Arrays.asList(nome));

        int cont = Collections.frequency(list2, "Aida");
        System.out.printf("Cont: %d%n",cont);

        // organiza a lista
        Collections.sort(list2);
        imprimeLista(list2);

        // muda 'Aida' para 'Bruna'
        Collections.replaceAll(list2, "Aida", "Bruna");
        imprimeLista(list2);

        // remove item da lista
        list2.remove("Bruna");
        removeItem(list2, 1, 6);
        imprimeLista(list2);

        /**
         * USANDO O Colloctions.binarySearch para procurar nome
         * procura por um nome e retorna a posição do mesmo
         * */
        System.out.printf("Encontrado na posição: %d%n",Collections.binarySearch(list2, "Tomazia"));

        // procura por um nome e retorna true caso encontra
        procurarNome(list2, "Brayen");

        // tentando de novo
        adicionarNome(list2, 2, "Brayen");
        procurarNome(list2, "Brayen");
        imprimeLista(list2);


        /**
         * Usando o LinkedList
         */

         LinkedList<String> ling = new LinkedList<>();
         ling.add("Java");
         ling.add("Kotlin");
         ling.add("C#");
         ling.add(2, "Python");// adicona na posição 2
         ling.addFirst("C");//adiciona na primeira posição
         ling.addLast("Julia");// adiciona na última posição

         for (String li : ling) {
             System.out.println(li.toUpperCase());
         }
    }

    // método para mostrar itens da lista
    private static void imprimeLista(List<String> list){
        System.out.println("***********************************");
        for(String i : list) {
            System.out.println(i);
        }
        System.out.println("***********************************");
    }

    // método para remover itens da lista
    private static void removeItem(List<String> list, int start, int end){
        list.subList(start, end).clear();
    }

    // método para encontrar um nome
    private static void procurarNome(List<String> list, String nome){
        if(list.contains(nome)){
            System.out.printf("Nome encontrado na posição: %d%n",list.indexOf(nome));
        } else {
            System.out.println("Erro: Nome não encontrado!");
        }
    }

    // método para adicionar elemento na lista
    private static void adicionarNome(List<String> list, int posicao, String nome) {
        list.add(posicao, nome);
    }
}

