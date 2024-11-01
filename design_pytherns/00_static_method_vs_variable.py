# Static Variables and Static Methods in Python
# Static Variables: In languages like C++ and Java, static variables inside functions are initialized once and retain their value between function calls. Python doesn’t have direct support for static variables within functions, but you can achieve similar functionality using class-level variables or function attributes.
# Static Methods: Static methods in Python, created with @staticmethod, belong to the class itself rather than instances. They don’t have access to instance-specific data (self) but can access class-level data if needed.
# Example: Robot Path Counter with Static Variables and Methods
# Here’s an example where we use static variables to count how many robots have been created and a static method to get the current robot count. The static variable is shared across all instances, and the static method allows access without needing an instance.

class Robot:
    robot_count = 0  # Static variable to count the number of robots created

    def __init__(self, name):
        self.name = name
        Robot.robot_count += 1  # Increment static variable each time a robot is created

    @staticmethod
    def get_robot_count():
        """Static method to get the current count of robots."""
        return Robot.robot_count

# Usage
robot1 = Robot("Robo1")
robot2 = Robot("Robo2")
robot3 = Robot("Robo3")

# Accessing static variable via static method
print(Robot.get_robot_count())  # Output: 3
# Explanation:
# Static Variable (robot_count): Declared at the class level, robot_count is shared among all Robot instances, keeping track of the total robot count.
# Static Method (get_robot_count): The @staticmethod decorator creates a method accessible directly on the class (Robot.get_robot_count()), allowing access to robot_count without creating an instance.
# Key Points:
# Static Variable (Class-Level): robot_count is persistent across all instances, providing a single shared variable that tracks the robot count.
# Static Method: get_robot_count provides class-level access to robot_count, showing how many robots have been created without requiring an instance of Robot.