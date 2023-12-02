using System.ComponentModel;
using System.IO;
using System.Runtime.CompilerServices;

namespace AdventOfCode;

public static class Program
{
    private static void Main(string[] args)
    {
        List<Game> games = MakeGames("../../../input.txt");
        Console.WriteLine(GetGamesSumOfPowers(games));
    }

    /// <summary>
    /// Gather all summed balls stored in corresponding Game objects.
    /// </summary>
    /// <param name="filePath">Path of file containing games.</param>
    /// <returns>List of produced games.</returns>
    private static List<Game> MakeGames(string? filePath)
    {
        List<Game> gamesToReturn = new List<Game>();
        StreamReader reader = new StreamReader(filePath);
        string? line;
        
        while ((line = reader.ReadLine()) != null)
        {
            gamesToReturn.Add(ProduceGame(line, gamesToReturn.Count + 1));
        }
        
        reader.Close();
        return gamesToReturn;
    }

    /// <summary>
    /// Produce game based on one line.
    /// </summary>
    /// <param name="line">Line to create game from.</param>
    /// <returns>Produced game.</returns>
    private static Game ProduceGame(string line, int id)
    {
        string[] fragments = line.Split(";");
        Game game = new Game();
        
        foreach (var fragment in fragments)
        {
            game.Id = id;
            
            // Add all balls of a specific color to a game
            game.Red.Add(FetchBalls(fragment, "red"));
            game.Green.Add(FetchBalls(fragment, "green"));
            game.Blue.Add(FetchBalls(fragment, "blue"));
        }
        
        return game;
    }

    /// <summary>
    /// Fetch all balls of a specific color within a single line.
    /// </summary>
    /// <param name="line">String we need to search through.</param>
    /// <param name="color">Color of the balls we need to find.</param>
    /// <returns>Amount of balls of a specific color in a singe game.</returns>
    private static int FetchBalls(string line, string color)
    {
        string[] fragments = line.Split(" ");
        int sum = 0;
        
        for (int i = 0; i < fragments.Length; i++)
        {
            if (fragments[i].Replace(",", "") == color)
            {
                sum += int.Parse(fragments[i - 1]);
            }
        }

        return sum;
    }
    
    /// <summary>
    /// Get sum of the power of games.
    /// </summary>
    /// <param name="games">Games to get sum for.</param>
    /// <returns>Sum of power of all valid games.</returns>
    private static int GetGamesSumOfPowers(List<Game> games)
    {
        int sum = 0;
        
        foreach (var game in games)
        {
            sum += game.Red.Max() * game.Green.Max() * game.Blue.Max();
        }

        return sum;
    }
}

struct Game
{
    public int Id;
    public List<int> Red;
    public List<int> Green;
    public List<int> Blue;

    public Game()
    {
        this.Red = new List<int>();
        this.Green = new List<int>();
        this.Blue = new List<int>();
    }
}