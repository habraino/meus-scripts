import java.time.LocalTime;
import java.util.Calendar;

/**
 * localTime
 */
public class localTime {

    public static void main(String[] args) {
        
        LocalTime sTime = LocalTime.now();
        System.out.println("default localtime: "+sTime);

        System.out.println("get only hours: "+sTime.getHour());
        System.out.println("get only minutes: "+sTime.getMinute());
        System.out.println("get only seconds: "+sTime.getSecond());

        Calendar calendar = Calendar.getInstance();
        System.out.println(calendar);

        
        
    }
}