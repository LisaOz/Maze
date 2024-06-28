# Maze

## Grid Path Calculator

This code provides a Python function to calculate the number of possible ways to movefrom the top-left 
corner to the bottom-right corner of an `n x m` grid. Movement is restricted to steps only dowm and
to the right side.

## Description
The `grid_paths` function uses dynamic programming to compute the number of unique paths in a grid. 
The function initializes a memoization table to store the number of ways to reach each cell in the grid 
and fills it based on the number of ways to reach the cells directly above and to the left of each cell.

## Installation
Clone this repository and run the Python script.

## Usage
To run the code, execute the script: python main.py.
You will be prompted to enter the dimensions of the grid (width and height).
The script will then calculate and print the number of possible paths from the top-left to the bottom-right 
corner of the grid.

## License
This project is licensed under the MIT License - see the see the LICENSE file for details.
