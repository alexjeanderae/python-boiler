#A generator is a type of function that allows you to iterate over a sequence of values without creating them all at once in memory. Instead of using return, a generator function uses yield to produce values one at a time, maintaining its state between calls.

def count_up_to(n):
    """Yields numbers from 1 up to n.

    Args:
        n (int): The max number to yield.

    Yields:
        int: The next number in the sequence.
    """
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)  # Prints numbers 1 through 5

# Explanation:
# yield: Temporarily pauses the function, returns a value, and remembers its position, allowing it to resume on the next call.
# Docstrings with Yields: In generators, the Yields section in a docstring describes the type and meaning of each yielded value, similar to Returns in regular functions.
# In Python, docstrings are used to describe a function’s behavior, arguments, return values, and more. When a function is a generator (i.e., it uses yield), it is common practice to describe what the generator yields instead of using the term "returns."

def read_lines(filename):
    """Open a file in read-only mode.

    Args:
        filename (str): The location of the file to read.

    Yields:
        str: Each line in the file.
    """
    with open(filename, 'r') as file:
        for line in file:
            yield line

# Explanation:

# The docstring provides a clear description of what the function does and what it expects (arguments).
# "Yields:" is used instead of "Returns:" because the function is a generator. This section describes what each yield statement will produce. In this case, it’s yielding strings, each representing a line from the file.