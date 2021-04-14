/**
 * aula08
 */
public class aula08 {

    public static void main(String[] args) {
        
        int[] arrayInt = new int[5];

        arrayInt[0] = 10;
        arrayInt[1] = 20;
        arrayInt[2] = 30;
        arrayInt[3] = 40;
        arrayInt[4] = 50;

        int soma1 = arrayInt[0] + arrayInt[1] + arrayInt[2];

        System.out.println("A soma dos três primeiros elementos é: "+soma1);

        int soma2 = 0;

        for(int i = 0; i < arrayInt.length; i++){
            soma2 += arrayInt[i];
        }
        System.out.println("A soma de todos os elementos é: "+soma2);
    }
}