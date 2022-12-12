# Other techniques in stack overflow see key_ideas.md

class Singleton(type):
    # Singleton inherits from type, that makes it a method also is a class object
    _instances = {}
    def __call__(cls, *args, **kwargs):
        # adding a call() method which is the getInstance() of the book
        if cls not in cls._instances:
            # no instance of the class yet - it instantiates one
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            # super is added to avoid an endless loop
        # there should be an instance by now, and it is returned
        return cls._instances[cls]

#Python3
class MyClass(metaclass=Singleton):
    pass # pass is placeholder here as we would expect such a class to have some key logic, def...

# classes are more more than way to make objects in python. They are .. objects themselves.
#  https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
# So you can do theses that other languages do not let you
# it's an object, and therefore:

# you can assign it to a variable
# you can copy it
# you can add attributes to it
# you can pass it as a function parameter

# the meta class is the stuff that creates a class object