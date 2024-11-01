# Memoization is an optimization technique where results of expensive function calls are stored, allowing the function to retrieve cached results instead of recalculating them. This is especially useful in recursive functions.

# Example in a practical scenario where it optimizes the calculation of unique paths in a grid (e.g., in robotics or pathfinding problems). Imagine a grid where you can only move right or down. We want to find the number of unique paths from the top-left corner to the bottom-right corner.

# Calculating Unique Paths in a Grid Using Memoization:

def unique_paths(m, n, memo={}):
    """Calculates the number of unique paths in an m x n grid.

    Args:
        m (int): The number of rows.
        n (int): The number of columns.

    Returns:
        int: The number of unique paths from the top-left to bottom-right.
    """
    # Base case: only one way to reach the edge
    if m == 1 or n == 1:
        return 1
    # Check if result is already in memo
    if (m, n) not in memo:
        # Recursively compute and store result in both directions
        memo[(m, n)] = unique_paths(m - 1, n, memo) + unique_paths(m, n - 1, memo)
    return memo[(m, n)]

# Example usage
# print(unique_paths(3, 3))  # Output: 6 (number of unique paths in a 3x3 grid)
# Explanation:
# Base Case: If the grid is 1 row or 1 column, there’s only 1 path.
# Memo Dictionary: Stores results for each (m, n) position to prevent redundant calculations.
# Efficiency: Memoization reduces redundant computations, making it feasible to compute paths in larger grids (e.g., 20x20) efficiently.