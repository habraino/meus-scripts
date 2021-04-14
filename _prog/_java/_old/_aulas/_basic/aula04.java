import java.util.Scanner;

public class aula04 {

    public static void main(String[] args) {
        
        int dia;
        String escolha;

        Scanner in = new Scanner(System.in);

        System.out.println("Qual seu dia da semana favorito? ");
        System.out.print("Digite 1 para segunda e 7 para domingo: ");
        dia = in.nextInt();
        
        escolha = (dia == 1) ? "segunda" :
              (dia == 2) ? "terça" :
              (dia == 3) ? "quata" :
              (dia == 4) ? "quinta" :
              (dia == 5) ? "sexta" :
              (dia == 6) ? "sábado" :
              (dia == 7) ? "domingo" :
                        "Dia inválido!";
        
        System.out.println("Você escolheu: "+escolha);

    }

}