/**
 * booleanTest
 */
public class booleanTest {

    public static void main(String[] args) {
        
        boolean foo = true;
        System.out.println("foo: "+foo);

        boolean bar = false;
        System.out.println("bar: "+bar);

        boolean notFoo = !foo;
        System.out.println("notFoo: "+notFoo);

        boolean fooAndBar = foo && bar;
        System.out.println("fooAndBar: "+fooAndBar);

        boolean fooOrBar = foo || bar;
        System.out.println("fooOrBar: "+fooOrBar);

        boolean fooXorBar = foo ^ bar;
        System.out.println("fooXorBar: "+fooXorBar);


    }
}