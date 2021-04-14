
/**
 * Fibonacci
 */
public class Fibonacci {

    // usando operadores condicionais
    public int calculaFibo(int n)
    {
        if(n == 1)
        {
            return 0;
        }else if(n == 2)
        {
            return 1;
        }else{
            return calculaFibo(n - 1) + calculaFibo(n - 2);
        }
    }

    // usando o operador condicinal ternário
    public int calculaFibo2(int n )
    {
        int val = (n == 1) ? 0 : (n == 2) ? 1 : calculaFibo2(n - 1) +  calculaFibo2(n - 2);

        return val;

    }
}
