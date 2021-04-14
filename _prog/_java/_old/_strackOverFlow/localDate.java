import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Date;

/**
 * localDate
 */
public class localDate {

    public static void main(String[] args) {
        
        // create a default date
        LocalDate lDate = LocalDate.now();
        int anoAtual = lDate.getYear();
        System.out.println("Ano atual é: "+anoAtual);
        System.out.printf("Já se passaram %d dias do ano.%n", lDate.getDayOfYear());

        // create a date from strings
        lDate = LocalDate.parse("2020-03-31");
        System.out.println("created date by string: "+lDate);


        // create a date from values
        lDate = LocalDate.of(2020, 03, 31);
        System.out.println("created date by values: "+lDate);

        // create a date from ZoneId
        lDate = LocalDate.now(ZoneId.systemDefault());
        System.out.println("crated date by ZoneId: "+lDate);

        // converting LocalDate to Date
        Date date = Date.from(Instant.now());
        ZoneId defaultZoneId = ZoneId.systemDefault();

        /* Date to LocalDate */
        LocalDate lDate1 = date.toInstant().atZone(defaultZoneId).toLocalDate();
        System.out.println("Date to LocalDate: "+lDate1);

        /* LocalDate to Date */
        Date date1 = Date.from(lDate1.atStartOfDay(defaultZoneId).toInstant());
        System.out.println("LocalDate to Date: "+date1);



    }
}