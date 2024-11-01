# Object Pool Pattern


# Here’s an example of the **Object Pool Pattern** adapted for a **robotics simulation** where reusable objects represent **Robot instances**. In robotics, instantiating a robot or preparing a robot for a task can be resource-intensive, especially if each robot needs specific initial configurations. An **Object Pool** can help manage these robot instances, offering them to clients as needed and returning them when the task completes.



# ### Robotics Example with Object Pool Pattern

# In this example:
# - **RobotPool** manages a fixed pool of `Robot` instances.
# - **Robot instances** are acquired for tasks, used temporarily, and then returned to the pool, making them available for other tasks.
# - This setup improves efficiency by avoiding repeated instantiation and configuration of `Robot` objects.


import random
import time

class Robot:
    """
    Represents a Robot that performs a task for a limited time.
    """
    def __init__(self, robot_id):
        self.robot_id = robot_id

    def perform_task(self, task):
        print(f"Robot {self.robot_id} is performing task: {task}")
        time.sleep(1)  # Simulate task duration
        print(f"Robot {self.robot_id} has completed task: {task}")


class RobotPool:
    """
    Manages a pool of Robot instances for task assignments.
    """
    def __init__(self, size):
        self._available_robots = [Robot(robot_id=i) for i in range(size)]

    def acquire_robot(self):
        if self._available_robots:
            return self._available_robots.pop()
        else:
            print("No robots available! Please wait.")
            return None

    def release_robot(self, robot):
        self._available_robots.append(robot)


# Simulation of a robotics system using the Object Pool pattern
def main():
    # Initialize a pool of 3 robots
    robot_pool = RobotPool(3)

    # Simulate tasks
    tasks = ["Inspect area", "Pick up item", "Navigate path"]

    # Acquire robots from the pool, perform tasks, and release them
    for task in tasks:
        robot = robot_pool.acquire_robot()
        if robot:
            robot.perform_task(task)
            robot_pool.release_robot(robot)
        else:
            print("Task cannot be performed as no robot is available.")

if __name__ == "__main__":
    main()


### Explanation

# 1. **Robot Class**:
#    - Represents an individual robot that performs a task. Each robot has a unique `robot_id` and a method `perform_task` to simulate performing a specific task.

# 2. **RobotPool Class**:
#    - Manages the pool of robots, keeping track of available robots in `_available_robots`.
#    - **acquire_robot**: Returns a robot from the pool if available; otherwise, it prints a message indicating no robots are free.
#    - **release_robot**: Returns a robot back to the pool, making it available for the next task.

# 3. **Usage in Main**:
#    - Creates a `RobotPool` with 3 robots.
#    - Simulates tasks by acquiring a robot from the pool, performing the task, and releasing the robot back to the pool.

# ### Key Benefits
# - **Efficiency**: By reusing robots rather than instantiating new ones for each task, the pool improves resource management.
# - **Performance**: This pattern is beneficial in scenarios where the setup or initialization of robots is costly and the pool size can satisfy concurrent needs without creating excessive instances.

# This approach makes the robotics system scalable while avoiding the high costs associated with frequent instantiation. The **Object Pool Pattern** is particularly useful when managing finite, expensive-to-create resources in a controlled way.