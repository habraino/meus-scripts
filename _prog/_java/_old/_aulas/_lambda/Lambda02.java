import java.util.List;
import java.util.function.Consumer;
import java.util.Arrays;

/**
 * Lambda02
 */
public class Lambda02 {

    public static void main(String[] args) {
        
        Aluno a1 = new Aluno("Brayen Strong", 30, "E");
        Aluno a2 = new Aluno("Hebraino Gomes", 35, "D");
        List<Aluno> a = Arrays.asList(a1, a2);
        
        a.forEach(x -> System.out.println(x.getNome()));
    }
}