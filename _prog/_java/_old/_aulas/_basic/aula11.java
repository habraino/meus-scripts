/**
 * aula11
 */
public class aula11 {

    public static void main(String[] args) {
        
        int[] nums = new int[4];

        nums[0] = 15;
        nums[1] = 19;
        nums[2] = 18;
        nums[3] = 20;

        int soma = 0; // armazena soma total
        float media = 0; // armazena media
        // calcula a soma total
        for(int item : nums){
            soma += item;
        }

        media = (float)soma / nums.length;

        System.out.println("A média eh: "+media);

        // imprime o menor e maior valor
        int menor = 0;
        int maior = 0;
        for(int item : nums){
            if(item < menor || menor == 0)
                menor = item;
            if(item > maior)
                maior = item;
        }

        System.out.println("Menor elemento: "+menor);
        System.out.println("Maior elemento: "+maior);

    }
}

