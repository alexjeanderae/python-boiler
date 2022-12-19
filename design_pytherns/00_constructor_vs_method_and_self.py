
# what is a constructor in python? Example of the main way to go.

# The first thing to remember is scope. 
# in python, there are four main namespace/ scopes. The one of the built-in function, that is the largest. Inside it, there is the 
# module global namespace. Then the class level name space, then the method. 
# All these scopes can have objects that need instantiation.

# Construtor is a special method used to create an instance of the class. In Python, the __init__ method is the most commonly used.
# When using the initializer method __init__ we have an instance of the class and we can put arguments pass on that method.
# It can be multiple arguments and will typically include self. self refers to the instance of the class itself and helps targeting # what is WITHIN it. 

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the # class. Writing this parameter as self is merely a convention. It is not a keyword and has no special meaning in Python. 
# We could use other names (like this ) but it is highly discouraged. Using names other than self is frowned upon by most developers
# and degrades the readability of the code (Readability counts). In other words the code below works, but smells:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(bla):
    print("Hello my name is " + bla.name)

p1 = Person("John", 36)
p1.myfunc()

# can we avoid constructors in python? What if we did not use it?
# the __init__.py file simply treats the directory as a package and creates a more tight environment to avoid collisions
# if you want to create an object you need to call init in the class method that creates the object. You cannot avoid it.
# Python will call it automatically for you. init only makes sure the object gets attached all the required properties. It 
# does not assign values.