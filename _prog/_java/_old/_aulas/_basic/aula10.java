/**
 * aula10
 */
public class aula10 {

    public static void main(String[] args) {
        
        int[][] array = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

        for(int x = 0; x < 3; x++){
            for(int y = 0; y < 3; y++){
                System.out.print(array[x][y] + "  ");
            }
            System.out.println("\n");
        }

    }
}