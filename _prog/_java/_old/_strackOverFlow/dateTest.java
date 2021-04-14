import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;

/**
 * dateTest
 */
public class dateTest {

    public static java.sql.Date convert(java.util.Date uDate) {
        java.sql.Date sDate = new java.sql.Date(uDate.getTime());

        return sDate;
    }

    public static void main(String[] args) {
        
        java.util.Date utilDate = new java.util.Date();
        System.out.println("java.util.Date is: "+utilDate);

        java.sql.Date sqlDate = convert(utilDate);
        System.out.println("java.sql.Date is: "+sqlDate);

        DateFormat df = new SimpleDateFormat("dd-MM-YYYY  hh:mm:ss");
        System.out.println("dateFormated is: "+df.format(utilDate));

        System.out.println("using java.util.Calendar is: "+new SimpleDateFormat("dd-MM-yyyy hh:mm.ss").format(Calendar.getInstance().getTime()));


    }
}