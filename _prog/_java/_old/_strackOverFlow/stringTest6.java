import java.util.Scanner;

/**
 * stringTest6
 */
public class stringTest6 {

    public static void main(String[] args) {
        
        String name = "brayen";
        System.out.println(name);

        StringBuilder sb = new StringBuilder(name);
        name = sb.reverse().toString();
        System.out.println(name);
        sb = sb.reverse();
        sb = sb.delete(1, 7);
        System.out.println(sb);

        String s = "spiral metal petal et al";
        System.out.println(s.replace("etal", "etalica"));
        System.out.println(s.replaceAll("(\\w*etal)", "$1lica"));

        String num = "";
        Scanner scanner = new Scanner(System.in);

        System.out.print("Informe um valor inteiro: ");
        num = scanner.next();
        StringBuilder sb1 = new StringBuilder(num);
        num = sb1.reverse().toString();
        scanner.close();

        System.out.println(num);
        System.out.println(Integer.parseInt(num) + 1);

    }
}

