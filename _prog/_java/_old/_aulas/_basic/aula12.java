/**
 * aula12
 */
public class aula12 {

    public static void main(String[] args) {
        
        int[][] nums = new int[10][10];

        for(int x = 0; x < nums.length; x++){
            String str = "";
            for(int y = 0; y < nums.length; y++){
                nums[x][y] = (3 * (x + 1) + (y * y));
                
                if(y < 9)
                    str += nums[x][y]+", ";
                else
                    str += nums[x][y];
            }
            System.out.println(str);
        }

    }
}