import java.util.Set;
import java.util.Map;
import java.util.HashMap;
import java.util.TreeSet;
import java.util.Scanner;

/**
 * Aula11
 */
public class Aula11 {

    public static void main(String[] args) {
        
        // cria HashMap para armazenar chaves de Strings e valores Integer
        Map<String, Integer> map = new HashMap<>();

        createMap(map);
        displayMap(map);

    }

    // cria mapa de entrada de usuário
    public static void createMap(Map<String, Integer> map) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter string: ");
        String input = in.nextLine();

        // tokeniza a entrada
        String[] tokens = input.split(" ");

        // processamento de texto de entrada
        for(String token : tokens) {
            String word = token.toLowerCase();

            // se o mapa contiver a palavra
            if(map.containsKey(word)) {
                int count = map.get(word); // obtém a contagem atual
                map.put(word, count + 1);
            } else {
                map.put(word, 1); // adiciona nova palavra com uma contagem de 1 para mapa
            }
        }
    }

    public static void displayMap(Map<String, Integer> map) {
        Set<String> keys = map.keySet();

        TreeSet<String> sortedKeys = new TreeSet<>(keys);

        System.out.printf("%nMap contains:%nKey\t\tValue%n");

        for (String key : sortedKeys) {
            System.out.printf("%-10s%10s%n", key, map.get(key) );
        }
        System.out.printf("%nsize: %d%nisEmpty: %b%n", map.size() , map.isEmpty());
    }
}

