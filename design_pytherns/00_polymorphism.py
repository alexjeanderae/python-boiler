# Polymorphism in Python

# Polymorphism allows a method to operate on different object types, enabling flexibility. It’s not about duplicating or substituting a class but about enabling a method to work across various implementations, provided they share common method names.
# The simple way to look is "this method of this class can work with other object types in other classes, just make sure the methods are named the same and have same arguments". 
# Only the method names and expected parameters need to match across different classes, not the actual method implementations (the "concrete methods"). Each class can define its own unique behavior inside the method as long as it follows the same interface or method signature

# So a simple example is to consider country objects that have a capital and a language. Then we do them the same and can start manipulating them - like loop through them.
class India:
    def capital(self):
        print("Governed from New Delhi")
        
    def language(self):
        print("talk Hindi and English")

class USA:
    def capital(self):
        print("Governed from Washington, D.C.")
        
    def language(self):
        print("talk English")

class Canada:
    def capital(self):
        print("Governed from Ottawa")
        
    def language(self):
        print("talk English and French")

# Polymorphic behavior
countries = [India(), USA(), Canada()]
for country in countries:
    country.capital()
    country.language()

# should output
# New Delhi
# Hindi and English
# Washington, D.C.
# English
# Ottawa
# English and French

# A more real life example can be payment where each time another implementation happens

#  Base interface or protocol (e.g., PaymentProcessor)
class PaymentProcessor:
    def process_payment(self, amount):
        """Process the payment of the specified amount."""
        pass

# CreditCard class implementation
class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

# PayPal class implementation
class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# BankTransfer class implementation
class BankTransfer(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")

# Usage of polymorphism
def complete_purchase(payment_method, amount):
    # `payment_method` can be any type that has a process_payment method
    payment_method.process_payment(amount)

# Example usage
purchase_amount = 100
payment_methods = [CreditCard(), PayPal(), BankTransfer()]

for method in payment_methods:
    complete_purchase(method, purchase_amount)

# Explanation:

# Polymorphic Behavior: Each PaymentProcessor subclass (e.g., CreditCard, PayPal, BankTransfer) implements process_payment. The complete_purchase function can accept any object with a process_payment method, enabling flexible and extensible handling of multiple payment types.
# Extensibility: Adding a new payment type (e.g., CryptoWallet) requires creating a new class with a process_payment method. The complete_purchase function remains unchanged, allowing the code to scale efficiently.