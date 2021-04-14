import java.util.Scanner;

/**
 * loop05
 */
public class loop05 {

    public static void main(String[] args) {
        
        Scanner scan = new Scanner(System.in);

        int n = 0;
        int cont = 1;
        double nota = 0;
        double media = 0;
        double soma = 0;
        double maior = 0 , menor = 0;

        // lê a quantidade dos alunos
        System.out.print("Informe o número de alunos: ");
        n = scan.nextInt();

        // se o valor informado for maior ou igual que 1 prossiga
        if(n >= 1){
            // enquanto n for maior ou igual que 1 prossiga
            while(cont <= n){
                
                // lê n nota e armazena em nota
                System.out.printf("Informe a %dª nota: ",cont);
                nota = scan.nextDouble();

                // enquanto a nota estiver fora do intervalo [0, 20]
                while((nota < 0) || (nota > 20)){
                    System.out.printf("Informe a %dª nota: ",cont);
                    nota = scan.nextDouble();
                }

                // pega maior e menor elemento
                if(cont == 1){
                    maior = nota;
                    menor = nota;
                }else{
                    if(nota > maior){
                        maior = nota;
                    }
                    if(nota < menor){
                        menor = nota;
                    }
                }

                soma += nota;// calcula a soma total das notas
                cont++;
            }

            media = soma / n;// calcula a média
            
            System.out.println("*************************************");
            System.out.println("Média é: "+media);
            System.out.println("Maior elemento: "+maior);
            System.out.println("Menor elemento: "+menor);
            System.out.println("*************************************");
        }else{ // senão
            System.out.println("Você digitou 0 alunos.\nPrograma fechou!!");
        }
    }
}