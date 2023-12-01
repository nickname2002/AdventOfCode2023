using System.IO;
using System.Runtime.CompilerServices;

namespace AdventOfCode;

public static class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine(GatherSum("../../../input.txt"));
    }

    /// <summary>
    /// Gathers the sum of all the first and last digits of the lines in a file.
    /// </summary>
    /// <param name="filePath">The filepath of the input file to read.</param>
    /// <returns>The sum of all the first and last digits of the lines in a file.</returns>
    private static int GatherSum(string? filePath)
    {
        StreamReader reader = new StreamReader(filePath);
        string? line;
        int sum = 0;
        
        // Process every line
        while ((line = reader.ReadLine()) != null)
        {
            (int, int) digits = GetFirstAndLastDigit(line);
            string numberToAdd = $"{digits.Item1}{digits.Item2}";
            sum += int.Parse(numberToAdd);
        }
        
        reader.Close();
        return sum;
    }

    /// <summary>
    /// Gathers the first and last integer digit of a string.
    /// </summary>
    /// <param name="line">Input string.</param>
    /// <returns>Tuple containing the first and last digit of a string.</returns>
    private static (int, int) GetFirstAndLastDigit(string line)
    {
        List<int> digits = new List<int>();

        // Scan for digits in the line
        foreach (var character in line)
        {
            if (char.IsNumber(character))
            {
                digits.Add(character - '0');
            }
        }

        return (digits.First(), digits.Last());
    }
}