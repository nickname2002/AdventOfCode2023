using System;
using System.IO;
using System.Collections.Generic;

namespace AdventOfCode
{
    public static class Game
    {
        static Dictionary<(int, int), List<int>> gearNumbers = new();
        
        private static void Main(string[] args)
        {
            List<List<char>> grid = MakeGrid("../../../input.txt");
            FindGearNumbers(grid);
            Console.WriteLine(ProcessGears());
        }

        /// <summary>
        /// Process the gears and return the sum of the ratios.
        /// </summary>
        /// <returns>Returns the sum of all gear ratios.</returns>
        private static int ProcessGears()
        {
            int sum = 0;
            
            foreach (var gear in gearNumbers)
            {
                if (gear.Value.Count == 2)
                {
                    int ratio = gear.Value[0] * gear.Value[1];
                    sum += ratio;
                }
            }

            return sum;
        }

        /// <summary>
        /// Find the numbers on the gears.
        /// </summary>
        /// <param name="grid">The grid to be searched through.</param>
        private static void FindGearNumbers(List<List<char>> grid)
        {
            for (int y = 0; y < grid.Count; y++)
            {
                for (int x = 0; x < grid[y].Count; x++)
                {
                    if (char.IsNumber(grid[y][x]))
                    {
                        int number = GetNumber(grid[y], x);
                        List<char> surroundedTiles = GetSurroundedTiles(grid, x, y, number.ToString().Length);
                        
                        // Check if it contains a '*'
                        if (surroundedTiles.Contains('*'))
                        {
                            List<(int, int)> gearPositions = GetPositionsOfGears(grid, x, y, number.ToString().Length);
                            
                            // Add gears to dictionary.
                            foreach (var gearPosition in gearPositions)
                            {
                                if (!gearNumbers.ContainsKey(gearPosition))
                                {
                                    gearNumbers.Add(gearPosition, new List<int>());
                                    gearNumbers[gearPosition].Add(number);
                                }
                                else
                                {
                                    gearNumbers[gearPosition].Add(number);
                                }
                            }
                        }
                        
                        // Update X position.
                        x += number.ToString().Length - 1;
                    }
                }
            }
        }
        
        /// <summary>
        /// Get the positions of the gears.
        /// </summary>
        /// <param name="grid">The grid to be searched through.</param>
        /// <param name="currentX">X position of the current tile.</param>
        /// <param name="currentY">Y position of the current tile.</param>
        /// <param name="numberLength">Length of the currently searched number.</param>
        /// <returns>A list of all adjacent gear positions.</returns>
        private static List<(int, int)> GetPositionsOfGears(List<List<char>> grid, int currentX, int currentY, int numberLength)
        {
            List<(int, int)> positions = new List<(int, int)>();

            // Get top tiles
            for (int x = currentX - 1; x <= currentX + numberLength; x++)
            {
                if (GetTileSafely(grid, x, currentY - 1) == '*')
                    positions.Add((x, currentY - 1));
                    
                if (GetTileSafely(grid, x, currentY + 1) == '*')
                    positions.Add((x, currentY + 1));
            }

            // Get middle tiles
            if (GetTileSafely(grid, currentX - 1, currentY) == '*')
                positions.Add((currentX - 1, currentY));
            
            if (GetTileSafely(grid, currentX + numberLength, currentY) == '*')
                positions.Add((currentX + numberLength, currentY));

            return positions;
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