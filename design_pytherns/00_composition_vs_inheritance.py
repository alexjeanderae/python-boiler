
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