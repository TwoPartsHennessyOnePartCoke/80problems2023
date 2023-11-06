/* AC, Принята */

using System;

class Program
{
    static int[,] MultiplyMatrices(int[,] A, int[,] B)
    {
        int n = A.GetLength(0);
        int[,] result = new int[n, n];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                for (int k = 0; k < n; k++)
                {
                    result[i, j] += A[i, k] * B[k, j];
                }
            }
        }
        return result;
    }

    static int[,] MatrixPower(int[,] matrix, int k)
    {
        int n = matrix.GetLength(0);
        int[,] result = new int[n, n];
        for (int i = 0; i < n; i++)
        {
            result[i, i] = 1;
        }

        while (k > 0)
        {
            if (k % 2 == 1)
            {
                result = MultiplyMatrices(result, matrix);
                k--;
            }
            else
            {
                matrix = MultiplyMatrices(matrix, matrix);
                k /= 2;
            }
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                result[i, j] = result[i, j] % 2 == 0 ? 1 : 0;
            }
        }

        return result;
    }

    static void Main()
    {
        string[] input = Console.ReadLine().Split(' ');
        int n = int.Parse(input[0]);
        int k = int.Parse(input[1]);
        int[,] matrix = new int[n, n];

        for (int i = 0; i < n; i++)
        {
            string line = Console.ReadLine();
            for (int j = 0; j < n; j++)
            {
                matrix[i, j] = int.Parse(line[j].ToString());
            }
        }

        int[,] result = MatrixPower(matrix, k);
        for (int i = 0; i < result.GetLength(0); i++)
        {
            for (int j = 0; j < result.GetLength(1); j++)
            {
                Console.Write(result[i, j]);
            }
            Console.WriteLine();
        }
    }
}
