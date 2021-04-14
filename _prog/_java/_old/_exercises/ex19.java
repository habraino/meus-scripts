/**
 * ex19
 * 
 * Leia um código de cinco algarismos (variável Codigo) e gere o digito verificador
(DigitoV) módulo 7 para o mesmo.
Supondo que os cinco algarismos do código são ABCDE, uma forma de calcular
o dígito desejado, com módulo 7 é:
DigitoV = resto da divisão de S por 7, onde
S = 6*A + 5*B + 4*C + 3*D + 2*E
 */

import java.util.Scanner;

public class ex19 {

    public static void main(String[] args) {
        
        /* cria uma nova instância da classe 'Scanner' */
        Scanner scanner = new Scanner(System.in);

        /* declaração das variáveis */
        int a, b, c, d, e;
        int s;
        int digitoV;
        
        /* lê o primeiro valor */
        System.out.print("Informe o primeiro valor: ");
        a = scanner.nextInt();

        /* lê o segundo valor */
        System.out.print("Informe o segundo valor: ");
        b = scanner.nextInt();

        /* lê o terceiro valor */
        System.out.print("Informe o terceiro valor: ");
        c = scanner.nextInt();

        /* lê o quarto valor */
        System.out.print("Informe o quarto valor: ");
        d = scanner.nextInt();

        /* lê o quinto valor */
        System.out.print("Informe o quinto valor: ");
        e = scanner.nextInt();

        /* fecha a classe Scanner */
        scanner.close();

        /* calcula o valor de 's' */
        s = 6*a + 5*b + 4*c + 3*d + 2*e;
        
        /* calcula modulo de s por 7 */
        digitoV = s % 7;

        /* mostra o resultado */
        System.out.printf("O dígito verificador é: %d%n", digitoV);

    }
}