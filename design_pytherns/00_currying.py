# Currying in Python

# My take is that currying isn’t always necessary, but in cases where functions need to be highly flexible and configurations vary widely, it’s a helpful technique for creating modular, reusable functions, that are easy to read. Essentially it tidies the code by having a better nesting of function and arguments.

# Non-curried functions: Take all arguments at once.
# Curried functions: Take arguments one at a time, returning a series of functions that each expect a single argument until all arguments are provided.

# From Stack Overflow: https://stackoverflow.com/questions/24881604/when-should-i-use-function-currying
# From https://www.stratascratch.com/blog/go-to-guide-to-currying-in-python/


# Original Function (non-curried):

def multiply(a, b, c):
    return a * b * c


# Curried Version:

def curried_multiply(a):
    """
    A curried version of multiply that takes one argument at a time.

    Parameters:
    a (int or float): The first number to multiply.

    Returns:
    function: A function that takes the second number, which in turn
              returns a function that takes the third number and 
              returns the final product.
    """
    def next(b):
        def final(c):
            return a * b * c
        return final
    return next

# You call it by passing all three arguments for instance
result = curried_multiply(2)(3)(4)  # Output: 24

# In the simplistic example above it almost feel that the non-curried is more pythonic. But it can be good to use currying to organize code. Like for instance our weather alert app.
# 

# In this example, we’ll create a base function that sends weather alerts, and then use currying to create specialized functions for different levels of warnings (like send_mild_alert and send_severe_alert), improving modularity and code reuse.

from functools import partial

def send_alert(alert_level, contact, message):
    """Sends an alert with a specified severity level."""
    print(f"[{alert_level}] Alert for {contact}: {message}")

# Create specialized functions for different alert levels using currying
send_mild_alert = partial(send_alert, "MILD")
send_severe_alert = partial(send_alert, "SEVERE")
send_critical_alert = partial(send_alert, "CRITICAL")

# Usage example in a weather alert system
def alert_contacts(contact_list, message, alert_func):
    for contact in contact_list:
        alert_func(contact, message)

# Example contact list and messages
contacts = ["Alice", "Bob", "Charlie"]
message = "Heavy rainfall expected in your area."

# Send mild, severe, and critical alerts by using the curried functions
alert_contacts(contacts, message, send_mild_alert)
alert_contacts(contacts, message, send_severe_alert)
alert_contacts(contacts, message, send_critical_alert)

# Explanation
# Base Function (send_alert): This function takes three parameters: alert_level, contact, and message. It serves as the foundation for all alert types.
# Curried Functions: Using partial, we create specialized versions of send_alert:
# send_mild_alert pre-fixes "MILD" as the alert level.
# send_severe_alert and send_critical_alert do the same for "SEVERE" and "CRITICAL".
# Modularity in Usage: The alert_contacts function can take any alert function as alert_func, allowing it to handle different severity levels without modifying its core logic. 

# Or currying with nesting like our payment example by having also a different currency

### Currying with Nesting in a Payment System

# In this example:
# 1. We start with a base function that processes a payment by taking a payment method, currency, and amount.
# 2. We create nested curried functions to specialize for **specific payment methods** and **currencies**, making the payment system highly modular.


from functools import partial

# Base function for processing payments
def process_payment(method, currency, amount):
    """Processes a payment with a specified method and currency."""
    print(f"Processing {currency} {amount} payment via {method}.")

# Step 1: Create curried functions for specific payment methods
credit_card_payment = partial(process_payment, "Credit Card")
paypal_payment = partial(process_payment, "PayPal")
bank_transfer_payment = partial(process_payment, "Bank Transfer")

# Step 2: Further nest to specify currency for each method
credit_card_usd = partial(credit_card_payment, "USD")
credit_card_eur = partial(credit_card_payment, "EUR")

paypal_usd = partial(paypal_payment, "USD")
paypal_eur = partial(paypal_payment, "EUR")

bank_transfer_usd = partial(bank_transfer_payment, "USD")
bank_transfer_eur = partial(bank_transfer_payment, "EUR")

# Usage example
def complete_transaction(payment_func, amount):
    payment_func(amount)

# Processing different payments
complete_transaction(credit_card_usd, 100)  # Output: Processing USD 100 payment via Credit Card.
complete_transaction(paypal_eur, 50)        # Output: Processing EUR 50 payment via PayPal.
complete_transaction(bank_transfer_usd, 200) # Output: Processing USD 200 payment via Bank Transfer.


### Explanation
# 1. **Base Function** (`process_payment`): Takes three arguments: `method`, `currency`, and `amount`. It prints out the payment details.
# 2. **Step 1 - Payment Method**: By using `partial`, we create specialized versions for each **payment method** (`credit_card_payment`, `paypal_payment`, and `bank_transfer_payment`).
# 3. **Step 2 - Currency Specialization**: We further nest by currying on currency, creating specific functions like `credit_card_usd`, `paypal_eur`, etc.
# 4. **Usage with `complete_transaction`**: The `complete_transaction` function accepts any of these specialized functions, making it easy to process payments in specific methods and currencies without modifying the main logic.

