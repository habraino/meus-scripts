/**
 * stringTest5
 */
public class stringTest5 {

    public static void main(String[] args) {
        
        StringBuilder sb = new StringBuilder("a");
        String s = sb.append("b").append(1).toString();
        System.out.println(s);

        System.out.println("============================");
        String name = "Brayen";
        String lastName = " Strong";
        String concated = name.concat(lastName);
        System.out.println(concated);
        
        System.out.println("============================");
        String example = "this is an example";
        String m1 = example.substring(11);
        String m2 = example.substring(5, 10);
        String m3 = example.substring(m1.length() - 3);
        System.out.println(m1);
        System.out.print(m2);
        System.out.println(m3);
        
        System.out.println("============================");
        String dateString = "2020年03月29日";
        dateString = dateString.substring(0, 4) + "-" + dateString.substring(5, 7) + "-" + dateString.substring(8, 10);
        System.out.println(dateString);
        
    }
}