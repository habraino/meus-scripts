import java.util.Scanner;

/**
 * loop07
 */
public class loop07 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);

        int totAlunos = 0; // armazena a quantidade dos alunos
        int contM = 0; // armazena quantidade dos alunos de sexo masculino
        int cont = 0; // contador
        int cont3 = 0; // contador dos alunos que presteram mais de 3 vezes
        int vez = 0; // vez que passou no vestibular
        int soma3 = 0;
        double media = 0;
        String sexo = ""; // sexo do aluno
        double sexoM = 0; // armazena media dos alunos de sexo masculino
        
        // armazena soma das vezes que os alunos de sexo masculino passou no vestibular
        int somaM = 0; 

        System.out.print("Informe a quantida total dos alunos: ");
        totAlunos = scan.nextInt();

        // enquanto o contador for menor ou igual a quantidade dos alunos
        while(sexo.toLowerCase() != "x"){
            System.out.print("Imforme o sexo do aluno(a)[m/f]: ");
            sexo = scan.next();

            if("x".equals(sexo.toLowerCase()))
                break;
            
            System.out.print("Quantas vezes esse aluno passou no vestibular? ");
            vez = scan.nextInt();

            if("m".equals(sexo.toLowerCase())){
                somaM += vez;
                contM++;
            }

            if(vez > 0)
                cont++;
            
            if(vez >= 3){
                soma3 += vez;
                cont3++;
            }
        }

        sexoM = somaM / contM;
        media = (double) soma3 / cont3;

        System.out.println(cont+" alunos passaram no vestibular.");

        System.out.println("A porcentagem de alunos do sexo masculino que passaram no vestibular é de: "+sexoM);

        System.out.println("Alunos que prestou vestibular 3 ou mais vezes no período: "+media+"%");
    }
}