# Let's break down the difference between `*args` and `**kwargs`, when to use them, what kind of objects they represent, and how to make sure you're passing the right one.


### 1. **What Are `*args` and `**kwargs`?**
# - **`*args`**: Used to pass a **variable number of positional arguments** to a function. These arguments are received as a **tuple**.
# - **`**kwargs`**: Used to pass a **variable number of keyword arguments** to a function. These arguments are received as a **dictionary**.

# ### 2. **When to Use `*args`**
# - Use `*args` when you want to allow a function to accept **any number of positional arguments**.
# - Examples:
#   - Functions where the number of arguments can vary, like a mathematical function that can add any number of numbers.
#   - Wrapping functions like in decorators where you don’t know how many arguments the wrapped function will take.

# **Example**:
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(10, 20))   # Output: 30

# - **Explanation**: `add_numbers` can take any number of arguments, and they are collected as a tuple called `args`.


### 3. **When to Use `**kwargs`**
# - Use `**kwargs` when you want to allow a function to accept **any number of keyword arguments**.
# - Examples:
#   - Functions that need to be highly configurable, like functions that format data based on various options.
#   - When you want to forward arguments to another function that takes many optional parameters.

# **Example**:

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, job="Engineer")
# Output:
# name: Alice
# age: 30
# job: Engineer

# - **Explanation**: `print_info` accepts any number of keyword arguments and processes them as a dictionary called `kwargs`.


### 4. **What Kind of Objects Are `*args` and `**kwargs`?**
# - **`*args`**: A tuple of all the positional arguments passed to the function.
# - **`**kwargs`**: A dictionary of all the keyword arguments passed to the function.

def example_function(*args, **kwargs):
    print(type(args))   # Output: <class 'tuple'>
    print(type(kwargs)) # Output: <class 'dict'>

example_function(1, 2, 3, a=4, b=5)


# ### 5. **How to Make Sure You’re Passing an `arg` or a `kwarg`?**
# - **Positional Arguments (`*args`)**: These are passed without explicitly naming them.
#   - **Correct**: `function(1, 2, 3)`
#   - **Incorrect**: `function(x=1, y=2)` (These would be keyword arguments)
# - **Keyword Arguments (`**kwargs`)**: These are passed by naming them explicitly.
#   - **Correct**: `function(x=1, y=2)`
#   - **Incorrect**: `function(1, 2)` (These would be positional arguments)

# **Example Function with Both**:

def mixed_args_function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"Additional positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

mixed_args_function(1, 2, 3, 4, x=5, y=6)
# Output:
# a: 1, b: 2
# Additional positional arguments: (3, 4)
# Keyword arguments: {'x': 5, 'y': 6}

### Summary of When to Use Each
# 1. **Use `*args`**:
#    - When you want to accept multiple **positional** arguments.
#    - When the exact number of arguments is not known in advance.
# 2. **Use `**kwargs`**:
#    - When you want to accept multiple **keyword** arguments.
#    - When you want to handle named parameters dynamically.

# ### Best Practices
# - Use `*args` for arguments that are **ordered** and where the order matters.
# - Use `**kwargs` for arguments that are **named** and usually serve as configuration options.
# - To ensure you’re passing `args` or `kwargs` correctly, remember:
#   - Positional arguments are passed **without naming**.
#   - Keyword arguments are passed **with a name**.

# Real life example using matplotlib

def custom_plot(x, y, *args, **kwargs):
    pass
# - **`x` and `y`**: These are **regular, positional arguments**. They are **required arguments** that must be explicitly provided when calling the function. Typically, in a plotting function like `custom_plot`, `x` and `y` represent the data points to be plotted (e.g., `x` could be the x-axis values and `y` could be the y-axis values).