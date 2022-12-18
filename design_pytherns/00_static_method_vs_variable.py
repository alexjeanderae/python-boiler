# see better the difference between static method and static variables in python

# from the singleton key_ideas.md
# A static variable inside a function is only visible inside that function's scope, but its lifetime is the entire life of the
#  program, and it's only initialized once). Basically, a persistent counter or storage variable that lives between function
# calls. Now, Python does not have static variables. But there are a few ways with different level of "hackiness" to get that
# effect. https://stackoverflow.com/q/279561/9065839
# Static can also apply to a method - not only on variables. "A static method in Java is a method that is part of a class rather than an instance of that class. Every instance of a class has access to the method. Static methods have access to class variables (static variables) without using the class's object (instance). Only static data may be accessed by a static method." 
# Python has a static method build it. https://www.javatpoint.com/static-in-python https://docs.python.org/3/library/functions.html#staticmethod https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python