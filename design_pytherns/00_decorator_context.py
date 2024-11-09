### Decorators

# **Decorators** are functions that **modify the behavior of other functions or methods**. They are often used for **logging**, **authentication**, **timing**, or **modifying outputs**. They set up a context, then run code on the context and finally remove the context.

# **Example: Timing Decorator**

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def example_task(duration):
    time.sleep(duration)

example_task(2)  # Outputs: example_task took 2.0001 seconds

# **Explanation**:
# - **`@timer`**: The decorator wraps `example_task` to add timing functionality, displaying how long it took to execute.


### Context Managers

# **Context managers** handle **setup and teardown** around a block of code, commonly using the `with` statement. They’re ideal for **resource management** like file handling or database connections.

# **Example: File Context Manager**

with open("example.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed after the block

# Custom context manager for timing
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield  # Run the block of code inside `with`
    end = time.time()
    print(f"Block took {end - start:.4f} seconds")

with timer():
    time.sleep(1)  # Block that we are timing


# **Explanation**:
# - **File Context Manager**: `with open(...) as file` opens a file, ensuring it is closed after the block.
# - **Custom Timer Context Manager**: Measures time around a block inside the `with` statement, similar to the timing decorator.

# Another usage of decorator is debugging. 
# Here we can build a decorator that return the type. Need a function that takes a function, a wrapper nested in it, doing something.

def print_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}() returned type {type(result)}")
        return result
    return wrapper

@print_return_type
def move_robot(direction):
    if direction in ["up", "down", "left", "right"]:
        return f"Moving {direction}"
    return None

print(move_robot("up"))       # Output: "move_robot() returned type <class 'str'>" and "Moving up"
print(move_robot("backward")) # Output: "move_robot() returned type <class 'NoneType'>" and None
