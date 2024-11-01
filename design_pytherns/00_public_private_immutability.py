# Public, private and immutability concepts in python by example

# Imagine a robot moving on a grid, where it can only move right or down. The robot’s starting position is the top-left corner (0, 0), and it needs to reach the bottom-right corner. We’ll use a class with public methods to control movement and private attributes to manage internal state. Additionally, the grid dimensions will be immutable once set.

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