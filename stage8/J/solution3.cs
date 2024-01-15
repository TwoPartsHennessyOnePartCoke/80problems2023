/* AC, Принята */

using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static List<int> SieveThing(int n)
    {
        var primes = new bool[n + 1];
        for (int i = 2; i <= n; i++)
            primes[i] = true;

        for (int p = 2; p * p <= n; p++)
        {
            if (primes[p])
            {
                for (int i = p * p; i <= n; i += p)
                    primes[i] = false;
            }
        }

        var primeNumbers = new List<int>();
        for (int i = 2; i <= n; i++)
        {
            if (primes[i])
                primeNumbers.Add(i);
        }

        return primeNumbers;
    }

    static void FindThreePrimes(int c, List<int> primes)
    {
        foreach (var i in primes)
        {
            if (i > c)
                break;

            int start = 0, end = primes.Count - 1;
            while (start <= end)
            {
                int sum = primes[start] + primes[end];
                if (sum == c - i)
                {
                    Console.WriteLine($"{c}={i}+{primes[start]}+{primes[end]}");
                    return;
                }
                else if (sum < c - i)
                    start++;
                else
                    end--;
            }
        }
        Console.WriteLine($"Для числа {c} гипотеза Гольдбаха неверна");
    }

    static void Main(string[] args)
    {
        var primes = SieveThing(1000000);

        int c;
        while ((c = Convert.ToInt32(Console.ReadLine())) != 0)
        {
            FindThreePrimes(c, primes);
        }
    }
}
