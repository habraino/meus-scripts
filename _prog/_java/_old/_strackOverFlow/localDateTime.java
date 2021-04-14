import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.Date;

/**
 * localDateTime
 */
public class localDateTime {

    public static void main(String[] args) {
        
        // create a default date
        LocalDateTime lDateTime = LocalDateTime.now();
        System.out.println("default dateTime: "+lDateTime);

        // create a date time from values
        lDateTime = LocalDateTime.of(2020, 03, 31, 23, 16);
        System.out.println("date time by values: "+lDateTime);

        // create a date time from string
        lDateTime = LocalDateTime.parse("2020-03-31T23:18");
        System.out.println("date time by string: "+lDateTime);
 
        // converting LocalDate to Date
        Date date = Date.from(Instant.now());
        ZoneId defaultZoneId = ZoneId.systemDefault();

        /* Date to LocalDate */
        LocalDateTime lDate = date.toInstant().atZone(defaultZoneId).toLocalDateTime();
        System.out.println("Date to LocalDate: "+lDate);

        /* LocalDate to Date */
        Date date1 = Date.from(lDate.atZone(defaultZoneId).toInstant());
        System.out.println("LocalDate to Date: "+date1);
    }
}