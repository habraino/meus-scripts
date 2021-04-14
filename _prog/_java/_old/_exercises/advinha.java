import java.security.SecureRandom;
import java.util.Collections;
import java.util.Scanner;

/**
 * advinha
 */
public class advinha {

    public static void main(String[] args) {

        SecureRandom sr = new SecureRandom();
        Scanner scanner = new Scanner(System.in);
        int pos = 0;
        String escolha = "";
        boolean sair = false;
        
        String[] charada = {"STP tem quantas estações?",
                            "Qual desses não é um ingrediente?",
                            "Em que ano foi descoberta a ilha de S.Tomé?",
                            "Qual é a cidade industrial de STP?",
                            "Qual é o maior rio de STP?",
                            "Qual destes não foi Presidente da República de STP?", 
                            "Como se chama o ritual usado para invocar demônio em STP?",
                            "STP é um país:",
                            "STP tem quantas línguas maternas?"};
        String[] res = {"2", "safú", "1470", "Neves", "Iô Grande", "Patrice Trovoada", "Djambi", "Democrático", "4"};

        String[][] opt = {{"2", "3", "4"}, {"safú", "tomate", "alho"}, {"1953", "1470", "1471"}, {"S.Tomé", "Guadalupe", "Neves"},
        {"Manuel Jorge", "Iô Grande", "Água Grande"}, {"Evaristo Carvalho", "Patrice Trovoada", "Pinto da Costa"}, {"Djambi", "Puita", "Tchiloli"},
        {"Burocrático", "Democrático", "Aristocrático"}, {"2", "3", "4"}};

        pos = sr.nextInt(charada.length);

        while(!sair){
        
            System.out.println(charada[pos]);
            for (int i = 0; i < 3; i++) {
                System.out.printf("a -> %s\nb -> %s\nc -> %s\n",opt[pos][0], opt[pos][1], opt[pos][2]);
                break;
            }

            escolha = scanner.nextLine();

            if(escolha.contains(res[pos])) {
                pos = sr.nextInt(charada.length);
                System.out.println(charada[pos]);
                
                for (int i = 0; i < 3; i++) {
                    System.out.printf("a -> %s\nb -> %s\nc -> %s\n",opt[pos][0], opt[pos][1], opt[pos][2]);
                    break;
                }
            } else {
                sair = true;
            }
            
        }
        /* fecha a classe Scanner */
        scanner.close();

    }

}