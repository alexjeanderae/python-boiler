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