import java.util.Scanner;

/**
 * Controler
 */
public class Controler {

    private String nome;
    private int idade;
    private String morada;

    private Scanner scan;
    
    public void pega(){
        Pessoa p = new Pessoa();
        scan = new Scanner(System.in);

        System.out.print("Nome: ");
        nome = scan.next();
    
        System.out.print("Idade: ");
        idade = scan.nextInt();

        System.out.print("Morada: ");
        morada = scan.next();

        p.setNome(nome);
        p.setIdade(idade);
        p.setMorada(morada);

    }

    public void obterTodos(){
        System.out.println("***************************************");
        System.out.printf("Nome............: %s\n",this.nome);
        System.out.printf("Idade...........: %d\n",this.idade);
        System.out.printf("Morada..........: %s\n\n",this.morada);
        System.out.println("***************************************");
    }
}