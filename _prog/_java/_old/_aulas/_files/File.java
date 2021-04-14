import java.io.IOException;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;

/**
 * File
 */
public class File {

    // função para ler o arquivo
    public static String Read(String path) {
        String conteudo = "";

        try {
            FileReader arq = new FileReader(path);
            BufferedReader lerArq = new BufferedReader(arq);
            String linha = "";

            try {
                linha = lerArq.readLine();
                while (linha != null) {
                    conteudo += linha;
                    linha = lerArq.readLine();
                }
                arq.close();
            } catch (IOException e) {
                System.out.println("Error: File not readed!");
            }
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found!");
        }

        // verifica se tem erro
        if(conteudo.contains("Error")) {
            return "";
        } else {
            return conteudo;
        }
    }

    // função para escrever no arquivo
    public static boolean Write(String path, String txt){
        try {
            FileWriter arq = new FileWriter(path);
            PrintWriter gravarArq = new PrintWriter(arq);
            gravarArq.println(txt);
            gravarArq.close();

            return true;
        } catch (IOException e) {
            System.err.println(e.getMessage());
            return false;
        }
    }
}