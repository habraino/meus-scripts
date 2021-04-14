import java.util.Scanner;

/**
 * ex46
 * 
 * Elaborar um algoritmo que lê três valores a, b, c e os escreve. A seguir, encontre
o maior dos três valores e o escreva com a mensagem : "É o maior”.
 */
public class ex46 {

    public static void main(String[] args) {
        
        // cria uma nova instância da classe 'Scanner'
        Scanner scanner = new Scanner(System.in);

        // declaração das variáveis
        int[] valores = new int[3];
        int maior = 0;
        int num;
        int cont = 0;

        // executa 3 vezes
        while (cont < 3) {
            // lê os 3 números
            System.out.printf("Informe o %dº número: ",cont+1);
            num = scanner.nextInt();
            valores[cont] = num; // adiciona o valor lido no vetor

            // verifica o maior número
            if (cont == 0) {
                maior = valores[cont];
            } else {
                if (valores[cont] > maior) {
                    maior = valores[cont];
                }
            }    
            cont++; // incrementa o contador
        }
        
        // apresenta os valores lidos na tela
        System.out.print("Valores lidos: [ ");
        for (int i : valores) {
            System.out.printf("%d ",i);
        }
        System.out.println("]");

        // mostra maior valor lido
        System.out.println("Maior é: "+maior);
        // fecha a classe 'Scanner'
        scanner.close();
    }
}