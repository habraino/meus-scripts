package caelum.poo;

public class TestaGerente {

    public static void main(String[] args) {
        
        ControleDeBonificacoes controle = new ControleDeBonificacoes();

        Gerente brayen = new Gerente();
        brayen.nome = "Brayen Strong";
        brayen.salario = 5000;
        controle.registra(brayen);


        System.out.printf("Nome do gerente: \033[1;35m%s\n\033[m",brayen.nome);

        System.out.println("Bonus anual do gerente: "+brayen.getBonificacao());

        System.out.println("********************************************");

        System.out.println(controle.getTotalDeBonificacoes());

    }

}