# Inheritance (Single Responsibility with Extension)
# You have a subclass that extends functionality from a parent class, but you want to retain the parent class’s behavior. For example, you have a base class Animal and a subclass Dog that adds additional functionality, but still uses the base behavior.

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent class __init__
        self.breed = breed

    def make_sound(self):
        base_sound = super().make_sound()  # Calling parent class method
        return f"{base_sound}, but {self.name} barks!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.make_sound())  # Output: "Some generic sound, but Buddy barks!"

# OK great, if it works can even use it as a pattern:
# Template Method Pattern: This is a pattern where a method in a superclass defines the structure of an operation, but allows subclasses to override certain steps. In the example above, Dog overrides make_sound() but still uses super() to call the parent’s version.
# Further read https://refactoring.guru/design-patterns/template-method

# But then it can lead to issues.
# Initialization in Multiple Inheritance and super() to the rescue
# The "diamond problem"  is an ambiguity that arises when two classes B and C inherit from A, and class D inherits from both B and C. 
# Source: https://en.wikipedia.org/wiki/Multiple_inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal: {self.name}")

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Mammal characteristics initialized.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Bird characteristics initialized.")

class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)
        print("Bat is both a mammal and a bird.")

# Usage
bat = Bat("Bruce")
# Output:
# Animal: Bruce
# Bird characteristics initialized.
# Mammal characteristics initialized.
# Bat is both a mammal and a bird.


# Why COMPOSITION is better than INHERITANCE - detailed Python example
# https://www.youtube.com/watch?v=0mcP8ZpUR38

# Inheritance is classes and subclasses. It is the "is" relationship vertically.
# While composition is borrowing from other classes at the same level. It is the "has" relationship horizontally.

# Using inheritance or composition enables single reponsibility or lowers code duplication. But inheritance adds strong coupling right off the bat.

# In python one of the way to code inheritence is through @dataclass - then an abstract class like class Employee(ABC) where the ABC has been 
# imported from the abc module. The classes that inherit from it, will be class HREmployee(Employee) or class SalesPerson(Employee) and all be
#  @dataclass
# You can also put methods in the abasctract class and decorate them with @abstractmethod. It also needs to be imported from abc module.''

# Composition would have a Employee class that borrows from a contract class and a commission class. The borrowing is happening though variables.


# Introduction to Python dataclasses
# https://www.youtube.com/watch?v=CvQ7e6yUtnw
# Aimed at helping to do more data oriented classes and improving performance. IT is an utility library.
# Can remove quite a lot of verbosity around class instantiation __init__, storage and representation of the object __repr__, and __eq__etc
# has also factory functions to make default values on non primitive data types


# Composition means that instead of inheriting from the external function (which isn’t possible), you compose new functionality around it.

# Here’s how you can do it:

from some_library import special_sum

class SpecialSumEnhancer:
    def __init__(self, additional_value):
        self.additional_value = additional_value

    def enhanced_sum(self, *args):
        # Use the existing function from the external library
        result = special_sum(*args)
        # Add custom behavior
        return result + self.additional_value

# Usage
enhancer = SpecialSumEnhancer(5)
print(enhancer.enhanced_sum(1, 2, 3))  # Example usage
# This keeps the logic clean and ensures that you can easily adapt if the special_sum behavior changes, as you are not relying on inheritance but instead just calling the function directly.

# Why Not Use Inheritance and super()?
# Inheritance is generally used when you want to extend or modify the behavior of a class. Since special_sum is a function, inheritance doesn’t apply here. If special_sum were a method of a class, then yes, you could potentially extend the class and use super() to call the method and add your own behavior. But in the case of a standalone function, the wrapping, composition, or decorator approach is much cleaner and more Pythonic.