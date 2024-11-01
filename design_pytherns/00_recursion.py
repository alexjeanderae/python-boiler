# Adapted from https://python-course.eu/advanced-python/recursive-functions.php

# Recursion is a method where a function calls itself to solve smaller instances of the same problem. It requires a base case to stop the recursion and prevent infinite loops.

# Example: Calculating Factorial Using Recursion:

def factorial(n):
    """Calculates the factorial of n using recursion.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Example usage
print(factorial(4))  # Output: 24 (4 * 3 * 2 * 1)
# Explanation:
# Base Case: n == 0 or n == 1, returns 1 to stop recursion.
# Recursive Case: n * factorial(n - 1), reduces the problem size with each call.
# Recursion breaks down 4! into 4 * 3 * 2 * 1 by solving smaller problems.