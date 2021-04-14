import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * exercise03
 */
public class exercise03 {

    public static void main(String[] args) {

        List<String> lista2 = new ArrayList<String>();
        lista2.add("Discliplinas");

        
        try {
            System.out.printf("[\033[33m***\033[m]Saída: \033[1;33m%s\033[m\n",lista2.get(0));
        } catch (Exception e) {
            //TODO: handle exception
            System.out.printf("[\033[0;31m***\033[m]Erro em: \033[1;31m%s\033[m\n",e);
        }
        
        List<String> lista = Arrays.asList(disc);
        lista.forEach(x -> {
            System.out.println(x);
        });
    }
    
    protected static String[] disc = {
        "Português", "Matemática", "Inglês", "Biologia II",
        "Ed.Física", "It.Social", "Francês"
    };
}