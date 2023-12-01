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
        SortedDictionary<int, string> foundDigits = new SortedDictionary<int, string>();
        List<string> possibleDigits = new List<string>
        {
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        };
        
        // Scan for digits in the line
        foreach (string digit in possibleDigits)
        {
            List<int> indexes = FindAllIndexesOfDigit(line, digit, possibleDigits.IndexOf(digit) + 1);
            
            foreach (var index in indexes)
            {
                foundDigits.Add(index, digit);
            }
        }

        // Get first and last digits
        string first = foundDigits.First().Value;
        string last = foundDigits.Last().Value;
        
        return (
            possibleDigits.IndexOf(first) + 1, 
            possibleDigits.IndexOf(last) + 1);
    }

    /// <summary>
    /// Find all occurrences of a digit (textual/numeric) within a line.
    /// </summary>
    /// <param name="line">Line to check for string occurrences.</param>
    /// <param name="str">String to find within the line.</param>
    /// <param name="nmbr">Numeric representation of `str`.</param>
    /// <returns>List of all indexes within the line where `str` is found.</returns>
    private static List<int> FindAllIndexesOfDigit(string line, string str, int nmbr)
    {
        List<int> indexes = new List<int>();
        int i = 0;
        
        // Gather all starting indexes of `str` within `line`
        while (i < line.Length)
        {
            try
            { 
                if (line.Substring(i, str.Length) == str 
                    || line[i].ToString() == nmbr.ToString())
                {
                    indexes.Add(i);
                }
            }
            catch (ArgumentOutOfRangeException e)
            {
                if (line[i].ToString() == nmbr.ToString())
                {
                    indexes.Add(i);
                }
            }
            
            i++;
        }

        return indexes;
    }
}