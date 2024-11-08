# Public, private and immutability concepts in python by example

# Imagine a robot moving on a grid, where it can only move right or down. The robot’s starting position is the top-left corner (0, 0), and it needs to reach the bottom-right corner. We’ll use a class with public methods to control movement and private attributes to manage internal state. Additionally, the grid dimensions will be immutable once set.

# Here we will achieve immutability by:
# Making rows and cols private and not providing setter methods to change them.
# Exposing these values only through a read-only property (grid_size), which provides access but not modification.

class Robot:
    def __init__(self, rows, cols):
        """Initialize a Robot with an immutable grid size."""
        self._rows = rows       # Private and immutable
        self._cols = cols       # Private and immutable
        self._position = (0, 0) # Private variable to track robot's current position

    @property
    def grid_size(self):
        """Public property to access grid size."""
        return (self._rows, self._cols)

    @property
    def position(self):
        """Public property to access current position."""
        return self._position

    def move_right(self):
        """Move the robot right if within grid limits."""
        if self._position[1] < self._cols - 1:
            self._position = (self._position[0], self._position[1] + 1)
        else:
            raise ValueError("Move out of bounds!")

    def move_down(self):
        """Move the robot down if within grid limits."""
        if self._position[0] < self._rows - 1:
            self._position = (self._position[0] + 1, self._position[1])
        else:
            raise ValueError("Move out of bounds!")

# Example usage
robot = Robot(3, 3)         # Create a 3x3 grid
print(robot.grid_size)      # (3, 3), immutable grid size
robot.move_right()          # Move to (0, 1)
robot.move_down()           # Move to (1, 1)
print(robot.position)       # (1, 1), current position

# robot._position = (2, 2)  # Error: Accessing private attribute directly

# Explanation:
# Immutability: grid_size (rows and cols) is set on initialization and can’t be modified, ensuring the robot's grid is fixed.
# Public Methods: move_right and move_down are public methods that allow controlled movement.
# Private State: _position and grid dimensions are private, ensuring that internal state changes only through defined methods.

# Recap:
# self._rows and self._cols are private and are not intended to be modified directly from outside the class.
# The grid_size property provides read-only access to these attributes, making the grid size effectively immutable.
# Public Properties:

# grid_size: A public property that allows access to the grid dimensions but prevents modification.
# position: A public property that allows external code to view the robot’s current position.
# Modifying State Safely:

# self._position is mutable because the robot's position needs to change as it moves.
# The move_right and move_down methods are public and provide controlled ways to change the robot's position while ensuring it doesn’t move out of the grid's bounds.

### Custom classes are by default not immutable
# By default, a **custom class** in Python, such as a `Car` class, is **mutable**. This means you can modify the attributes of an instance of the class after it has been created.

### Example of a Mutable Custom Class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating an instance of Car
my_car = Car("Toyota", "Camry", 2020)

# Modifying the attributes of my_car
my_car.year = 2021
print(my_car.year)  # Output: 2021

# **Explanation**:
# - In the example above, `my_car` is an instance of `Car`, and we can easily change the `year` attribute, demonstrating that the class is **mutable** by default.

### How to Make a Custom Class Immutable

# If you want to make your `Car` class immutable, you need to override certain behaviors to prevent modifications to the attributes after the object is created. One way to achieve this is by using the `__slots__` attribute or by overriding attribute setting methods.

#### Method 1: Using `__slots__` to Restrict Attribute Changes
# The `__slots__` attribute can restrict the creation of new attributes but doesn't completely make the class immutable.


class Car:
    __slots__ = ('make', 'model', 'year')

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Example
my_car = Car("Toyota", "Camry", 2020)
# my_car.year = 2021  # This still allows changing the existing attribute
# my_car.color = "Red"  # Raises AttributeError: 'Car' object has no attribute 'color'


# - **Explanation**: Using `__slots__` prevents the addition of new attributes but does not make the class fully immutable.

#### Method 2: Using Read-Only Properties
# A more effective way to make a class immutable is by using **read-only properties**.

class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

# Example
my_car = Car("Toyota", "Camry", 2020)
# my_car.year = 2021  # Raises AttributeError: can't set attribute
print(my_car.year)  # Output: 2020

# - **Explanation**: Using the `@property` decorator, we make the attributes **read-only**, which means they cannot be modified after the object is created.

#### Method 3: Using `namedtuple` for Simple Immutable Classes
# For simpler cases, you can use `namedtuple` from the `collections` module to create an immutable class-like structure.


from collections import namedtuple

Car = namedtuple('Car', ['make', 'model', 'year'])
my_car = Car("Toyota", "Camry", 2020)

# my_car.year = 2021  # Raises AttributeError: can't set attribute
print(my_car.year)  # Output: 2020


# - **Explanation**: `namedtuple` creates an immutable class-like object where attributes cannot be reassigned.

### Summary
# - By default, a custom class like `Car` is **mutable**.
# - To make a custom class **immutable**, you can:
#   - Use **read-only properties** with `@property` decorators.
#   - Use `namedtuple` for simple, immutable data structures.
#   - Use `__slots__` to restrict the creation of new attributes, though this alone does not make the class fully immutable.
  
# Making a class immutable can be useful for ensuring that the state of an object remains constant once it is created, similar to the behavior of immutable data types like strings or tuples in Python.

### What about wanting to make a "parent" variable mutable? The non local keyword in nested functions
# The nonlocal keyword is used in a nested function to modify a variable from the enclosing (non-global) scope. This is useful for maintaining state across function calls, like in a counter example.


def create_counter():
    count = 0  # Enclosing variable, initially immutable - an integer (immutable) but mostly because out of the scope of the "child"

    def increment(): # count variable is NOT passed
        nonlocal count  # Use nonlocal to modify 'count' in the "parent" function
        count += 1
        return count

    return increment

counter = create_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
# Explanation
# Without nonlocal: count would be treated as a local variable inside increment, and modifying it would have no effect on the count in create_counter.
# With nonlocal: We can change count, which is otherwise immutable in the enclosing scope. Using nonlocal makes count behave like a mutable variable, allowing its value to be updated.
# Tying It Back to Mutability
# Normally, variables like count (an integer) are immutable. However, nonlocal lets us treat count as if it were mutable, enabling in-place modification of its value across function calls.
# This gives a sense of mutability within closures, even for otherwise immutable types like integers.

# And no, we couldn’t have simply passed `count` as a parameter to `increment` to achieve the same effect. If we passed `count` as an argument to `increment`, it would create a **local copy** of `count` within `increment`, and any modifications would only affect that local copy, leaving the original `count` in the enclosing scope unchanged. This is because integers are **immutable**, and any operation that "modifies" an integer actually creates a new integer object.

### Example Using `count` as a Parameter (wrong way)

def create_counter():
    count = 0  # Enclosing variable

    def increment(count):  # Takes count as a parameter this time
        count += 1  # Modifies the local copy of count
        return count

    return increment

counter = create_counter()
print(counter(0))  # Output: 1
print(counter(1))  # Output: 2


### What `nonlocal` Does Differently
# The `nonlocal` keyword allows `increment` to **modify the `count` variable from the enclosing scope** directly. Instead of creating a new local variable, `nonlocal` makes `count` in `increment` refer to the same `count` in `create_counter`.