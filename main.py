'''
This script calculates the number of possible ways out of the maze
using the dynamic programming with memoization
'''


def grid_paths(n, m):
    # Initialise the dictionary to store the number of ways to reach each cell
    memo = {}

    # Define the base case with one possible way to reach the cell in the first row or the first column
    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1

    # Fill the memo table for the rest of the grid
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]

        # Return the number of ways to reach the bottom-right corner
    return memo[(n, m)]


# Get grid dimensions from the user
grid_width = int(input("Enter your grid dimensions, width: "))
grid_height = int(input("Enter you grid dimensions, height: "))

# Calculate the number of paths
paths = grid_paths(grid_height, grid_width)

# print the number of paths
print(f"Number of possible ways through a {grid_height}x{grid_width} is: {paths}")