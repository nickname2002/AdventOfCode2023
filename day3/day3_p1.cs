using System;
using System.IO;
using System.Collections.Generic;

namespace AdventOfCode
{
    public static class Game
    {
        private static void Main(string[] args)
        {
            List<List<char>> grid = MakeGrid("../../../input.txt");
            Console.WriteLine(ProcessGrid(grid));
        }

        /// <summary>
        /// Processes the grid and returns the sum of all numbers that are valid.
        /// </summary>
        /// <param name="grid">Grid to search through.</param>
        /// <returns>The sum of all numbers that are valid.</returns>
        private static int ProcessGrid(List<List<char>> grid)
        {
            int sum = 0;

            for (int y = 0; y < grid.Count; y++)
            {
                for (int x = 0; x < grid[y].Count; x++)
                {
                    if (char.IsNumber(grid[y][x]))
                    {
                        // Get the entire number sequence we're visiting.
                        int number = GetNumber(grid[y], x);
                        Console.WriteLine(number);

                        // Check whether the number should be added to the sum.
                        if (IsValidNumber(grid, x, y, number.ToString().Length))
                        {
                            sum += number;
                        }

                        // Change the index to check.
                        x += number.ToString().Length - 1;
                    }
                }
            }

            return sum;
        }

        /// <summary>
        /// Checking whether the number is valid.
        /// </summary>
        /// <param name="grid">Grid to search through.</param>
        /// <param name="currentX">The X position of the current tile.</param>
        /// <param name="currentY">The Y position of the current tile.</param>
        /// <param name="numberLength">The length of the current number.</param>
        /// <returns></returns>
        private static bool IsValidNumber(List<List<char>> grid, int currentX, int currentY, int numberLength)
        {
            List<char> surroundedTiles = GetSurroundedTiles(grid, currentX, currentY, numberLength);

            foreach (var tile in surroundedTiles)
            {
                if (tile != '.')
                {
                    return true;
                }
            }

            return false;
        }
        
        /// <summary>
        /// Get the tiles surrounding the current number.
        /// </summary>
        /// <param name="grid">Grid to search through.</param>
        /// <param name="currentX">The X position of the current tile.</param>
        /// <param name="currentY">The Y position of the current tile.</param>
        /// <param name="numberLength">The length of the current number.</param>
        /// <returns></returns>
        private static List<char> GetSurroundedTiles(List<List<char>> grid, int currentX, int currentY, int numberLength)
        {
            List<char> surroundedTiles = new List<char>();

            // Get top tiles
            for (int x = currentX - 1; x <= currentX + numberLength; x++)
            {
                surroundedTiles.Add(GetTileSafely(grid, x, currentY - 1));
                surroundedTiles.Add(GetTileSafely(grid, x, currentY + 1));
            }

            // Get middle tiles
            surroundedTiles.Add(GetTileSafely(grid, currentX - 1, currentY));
            surroundedTiles.Add(GetTileSafely(grid, currentX + numberLength, currentY));

            return surroundedTiles;
        }

        /// <summary>
        /// Get the tile at the given position. If the position is out of bounds, return a dot.
        /// </summary>
        /// <param name="grid">Grid to search through.</param>
        /// <param name="x">The X position of the current tile.</param>
        /// <param name="y">The Y position of the current tile.</param>
        /// <returns></returns>
        private static char GetTileSafely(List<List<char>> grid, int x, int y)
        {
            try
            {
                return grid[y][x];
            }
            catch (ArgumentOutOfRangeException)
            {
                return '.';
            }
        }

        /// <summary>
        /// Get the number at the given position.
        /// </summary>
        /// <param name="row">Get the row to search through.</param>
        /// <param name="currentX">The X position of the current tile.</param>
        /// <returns>The currently selected number.</returns>
        private static int GetNumber(List<char> row, int currentX)
        {
            string numberBuffer = "";

            for (int x = currentX; x < row.Count; x++)
            {
                if (!char.IsNumber(row[x]))
                {
                    return int.Parse(numberBuffer);
                }

                numberBuffer += row[x];
            }

            return int.Parse(numberBuffer);
        }

        /// <summary>
        /// Make a grid from the given file path.
        /// </summary>
        /// <param name="filePath">The filepath to produce a grid for.</param>
        /// <returns>The grid produced from the filepath.</returns>
        private static List<List<char>> MakeGrid(string filePath)
        {
            List<List<char>> grid = new List<List<char>>();
            StreamReader r = new StreamReader(filePath);
            string? line;
            int y = 0;

            while ((line = r.ReadLine()) != null)
            {
                grid.Add(new List<char>());

                foreach (var t in line)
                {
                    grid[y].Add(t);
                }

                y++;
            }

            r.Close();
            return grid;
        }
    }
}
