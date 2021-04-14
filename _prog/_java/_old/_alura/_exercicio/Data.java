import java.text.SimpleDateFormat;
import java.util.Date;

public class Data {

    public static void main(String[] args) {
        
        Date data = new Date();
        SimpleDateFormat formatar = new SimpleDateFormat("dd-MM-Y HH:mm:ss");
        String dataFormatada = formatar.format(data);
        
        System.out.println(dataFormatada);
        
    }
    
}