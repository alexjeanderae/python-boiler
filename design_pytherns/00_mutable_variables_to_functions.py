# In Python, **passing mutable variables** (like lists, dictionaries, dataframes, numpy vectors or custom objects) to functions can have some **unexpected effects** if you're not careful, due to how Python handles variable references. When you use a mutable object as a default argument in a function, that object **persists across multiple calls** to the function, rather than being reinitialized each time.

# ### How Passing Variables Works in Python
# 1. **Pass-by-Reference**: When you pass a **mutable object** (like a list or dictionary) to a function, you’re passing a **reference** to the original object, not a copy. This means changes made to the object inside the function will **affect the original object**.
# 2. **Pass-by-Value**: For **immutable objects** (like integers, strings, or tuples), Python passes a **copy of the value**, so changes inside the function won’t affect the original value.

### Example of Mutable Variables - Intended!

def modify_list(my_list):
    my_list.append(10)  # Modifies the original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)  # Output: [1, 2, 3, 10]


# **Explanation**:
# - The `modify_list` function adds `10` to `my_list`. Since `my_list` is a reference to the original `numbers` list, the modification is reflected in `numbers`.

### How to Avoid Unintended Modifications
# If you want to **avoid modifying the original mutable object**, you can create a **copy** of it before making changes.


def safe_modify_list(my_list):
    my_copy = my_list.copy()  # Make a shallow copy
    my_copy.append(10)
    return my_copy

numbers = [1, 2, 3]
new_numbers = safe_modify_list(numbers)
print(numbers)      # Output: [1, 2, 3] (unchanged)
print(new_numbers)  # Output: [1, 2, 3, 10]

### Key Points
# 1. **Mutable Objects**: Lists, dictionaries, sets, and most numpy objects are mutable. Be cautious when passing them to functions, as changes inside the function can alter the original object.
# 2. **Immutable Objects**: Integers, strings, tuples, and frozensets are immutable. When passed to a function, the original value remains unaffected by any changes.
# 3. **Shallow vs. Deep Copy**:
#    - **Shallow Copy**: Only copies the outer structure (e.g., `my_list.copy()`). If the list contains other mutable objects, they will still be referenced (ie can have unintended consequences).
#    - **Deep Copy**: Creates a full copy of the object and all objects nested within it. Use the `copy` module: `import copy; deep_copy = copy.deepcopy(my_list)` (ie no expected unintended consequences)

# ### Practical Example
# In scenarios where you’re dealing with **complex data structures** (like a list of dictionaries), using a **deep copy** may be necessary to ensure the original structure is not modified.


import copy

def modify_deep(my_data):
    deep_copy = copy.deepcopy(my_data)
    deep_copy[0]['key'] = 'new_value'  # Only affects the deep copy
    return deep_copy

data = [{'key': 'value'}, {'key': 'another_value'}]
new_data = modify_deep(data)
print(data)      # Output: [{'key': 'value'}, {'key': 'another_value'}] (unchanged)
print(new_data)  # Output: [{'key': 'new_value'}, {'key': 'another_value'}]


# Other option using `None` as the default argument in a function 
### Example of the Problem with Mutable Defaults in dataframes

def add_column(values, df=pandas.DataFrame()):
    df['col_{}'.format(len(df.columns))] = values
    return df

# Call the function twice
result1 = add_column([1, 2, 3])
result2 = add_column([4, 5, 6])

print(result1)
print(result2)  # result2 will contain both columns, which is unexpected and probably not desired

### Why `None` Solves the Problem
# To avoid this issue, you use `None` as the default value and then initialize the mutable object (like a DataFrame) **inside the function**. This ensures that a **new DataFrame** is created each time the function is called if `df` is not provided.

### Revised Function

def better_add_column(values, df=None):
    """Add a column of `values` to a DataFrame `df`."""
    if df is None:  # Only create a new DataFrame if df is not provided
        df = pandas.DataFrame()
    df['col_{}'.format(len(df.columns))] = values
    return df

### Explanation of `None` as the Default Argument
# - **df=None**: Using `None` as the default argument ensures that a new DataFrame is created each time the function is called if `df` is not provided by the user.
# - **if df is None**: Inside the function, you check if `df` is `None` and then initialize a new DataFrame. This way, the DataFrame is not shared across multiple calls.

### Summary
# - **Mutable variables** passed to functions can be modified, affecting the original data.
# - To prevent unintended side effects, use **copies** (shallow or deep) of mutable objects.
# - Understanding how Python handles variable references can help you write more predictable and bug-free code.
# - String is not mutable while list are mutable. A lot of operations on strings return a new string then reassign. Most Numpy objects are mutable.
# - **Using `None`**: By setting the default argument to `None` and creating the DataFrame inside the function, you ensure that a new, independent DataFrame is created each time, preventing unexpected behavior.