import java.util.Scanner;

/**
 * first
 */
public class first {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        String file = "teste.txt";

        String txt = "";
        
        System.out.print("Text: ");
        txt = scanner.nextLine();

        // escrever dados
        if(File.Write(file, txt)) {
            System.out.println("Salvo com sucesso!");
        } else {
            System.out.println("Erro ao salvar!");
        }

        // ler dados
        String texto = File.Read(file);

        if(texto.isEmpty()) {
            System.out.println("Erro ao ler!");
        } else {
            System.out.printf("\033[1;36m%s\033[m\n",texto);
        }

    }
    
}