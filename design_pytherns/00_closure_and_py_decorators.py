# Closure and decorators in Python

# a closure is a type of nested function. You expect to see a def inside a def. It is a function object.
# it has a kind of higher scope and persistence.
# "Closure in Python is an inner function object, a function that behaves like an object, that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing."
# it will generally finish with a return

def f1(x):
	def f2(y):
		return x + y
	return f2

adder = f1(12)
print(adder(4))
# >>> returns 16

# a example of a decorator (the idea is a function that extends another)

buy_price = .89

def sale(func):
    def calc():
        print('Special pricing this week only: $', round(func() * 0.8, 2), 'Save 20%!')
    return calc()

@sale
def markup():
    retail_price = (buy_price * 1.76)
    print('Normal retail price: $', round(retail_price, 2))
    return retail_price

markup

# Result
'''
Normal retail price: $ 1.57
Special pricing this week only: $ 1.25 Save 20%!
'''

# is equivalent to 

buy_price = .89

def sale(func):
    def calc():
        print('Special pricing this week only: $', round(func() * 0.8, 2), 'Save 20%!')
    return calc()

def markup():
    retail_price = (buy_price * 1.76)
    print('Normal retail price: $', round(retail_price, 2))
    return retail_price

sale(markup)

# Result

# >>> Normal retail price: $ 1.57
# >>> Special pricing this week only: $ 1.25 Save 20%!


# Decorator Pattern Using Inheritance
# Scenario:
# The Decorator Pattern can be used to dynamically add behavior to an object. In this case, super() can be used to extend functionality dynamically, while still using base functionality. Instead of function decorators, here we’re using class-based decorators to wrap and extend behavior.

#Example:

class Document:
    def __init__(self, content):
        self.content = content

    def display(self):
        return self.content

class EncryptedDocument(Document):
    def display(self):
        base_display = super().display()  # Calling the parent class method
        return f"Encrypted: {base_display[::-1]}"  # Simulate encryption by reversing text

class SignedDocument(Document):
    def display(self):
        base_display = super().display()
        return f"{base_display} [Signed]"

# Usage
doc = Document("This is a sensitive document.")
encrypted_doc = EncryptedDocument("This is a sensitive document.")
signed_doc = SignedDocument("This is a sensitive document.")

print(doc.display())  # Output: This is a sensitive document.
print(encrypted_doc.display())  # Output: Encrypted: .tnemucod evitisnes a si sihT
print(signed_doc.display())  # Output: This is a sensitive document. [Signed]


#Decorator Pattern: super() is used to extend the base class’s functionality. The derived classes modify the behavior of display() while still using the original functionality via super().
# When to Use super():
# In class-based decorators, when you want to wrap and extend the behavior of an existing class method.
# Key Points for Using super():
# Single Inheritance: Use super() when you want to call the parent class’s method within a method that has been overridden in the subclass.
# Multiple Inheritance: super() is crucial when dealing with complex inheritance hierarchies to ensure that all parent classes are correctly initialized or their methods are called in the right order.
# PEP 8 Recommendation: Always use super() rather than directly calling the parent class (e.g., ParentClass.method(self)), as super() ensures proper method resolution order (MRO), making your code more maintainable and less prone to errors in complex hierarchies.
# Pythonic Use of super():
# Cleaner code: super() provides a more maintainable and extensible solution than directly invoking base class methods.
# Avoid name collisions: Using super() helps avoid issues with multiple inheritance and ensures that the method resolution order (MRO) is respected.