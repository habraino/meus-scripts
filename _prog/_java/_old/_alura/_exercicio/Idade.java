import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.Scanner;
/**
 * Idade
 */
public class Idade {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        Date data = new Date();
        SimpleDateFormat dataFormatado = new SimpleDateFormat("YYYY");

        int idade, nasc;
        int atual = Integer.parseInt(dataFormatado.format(data)); // pega o ano atual

        System.out.print("Informe seu ano de nascimento: ");
        nasc = in.nextInt(); // pega o ano de nascimento

        idade = atual - nasc; // calcula a idade

        System.out.printf("Você tem %d anos.\n", idade);

    }
}