/**
 * aula09
 */
public class aula09 {

    public static void main(String[] args) {
        
        int[][] array = new int[3][4];

        array[0][0] = 10;
        array[0][1] = 20;
        array[0][2] = 30;
        array[0][3] = 40;

        for(int i = 0; i < array[0].length; i++){
            System.out.println(array[0][i]);
        }

    }
}
