import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

/**
 * Lambda01
 */
public class Lambda01 {

    public static void main(String[] args) {
        
       // Mostrador mostrador = new Mostrador();

        Aluno a1 = new Aluno("Aida Araújo", 3, "D");
        Aluno a2 = new Aluno("Hebraino de Deus ", 30, "D");
        Aluno a3 = new Aluno("Jailson Lopes", 34, "D");

        List<Aluno> alunos = Arrays.asList(a1, a2, a3);

        // função anónima para cosumir dados do Aluno
        /*Consumer<Aluno> mostrador = new Consumer<Aluno>() {
            public void accept(Aluno a){
                System.out.println(a.getNome());
            }
        };*/
        alunos.forEach(new Consumer<Aluno>() {
            public void accept(Aluno a){
                System.out.println(a.getNumero());
            }
        });// método forEach()
    }
}

