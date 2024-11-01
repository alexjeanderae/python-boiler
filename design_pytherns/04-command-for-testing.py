# Command Pattern encapsulates distinct commands, you can write doctests in the docstrings for each command, providing examples of how each command is used and verifying their basic functionality. 
# Structure Overview:
# Doctests: Add docstring-based tests (doctests) for individual commands to check simple behaviors like shrinking CSS, handling screenshots, etc.
# pytest: Use pytest to handle more complex testing, like running Selenium-based tests, verifying images processed by Pillow, or ensuring that the command sequence is executed correctly.
# Command Pattern: You’ll use the Command Pattern to organize and run these commands.

# For illustration, let's do some basic sales  calculations. We’ll implement three commands:
# CalculateRevenueCommand: Calculates total revenue based on price and quantity.
# ApplyDiscountCommand: Applies a discount to the total revenue.
# CalculateNetRevenueCommand: Calculates net revenue after applying taxes and other deductions.

# Each command will be encapsulated in its own class with an execute method. We’ll add doctests for basic functionality within each command, and later we could use pytest to test command sequences or more complex scenarios.

# Step 1: Define the Command Interface and Concrete Commands with Doctests
# First, we define an abstract Command class that each command will inherit from:

from abc import ABC, abstractmethod

class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass
# CalculateRevenueCommand
# This command calculates revenue based on unit price and quantity sold.

class CalculateRevenueCommand(Command):
    """
    Calculates total revenue based on price per unit and quantity.

    Parameters:
    price (float): Price per unit.
    quantity (int): Quantity sold.

    Examples:
    >>> revenue_cmd = CalculateRevenueCommand(10.0, 5)
    >>> revenue_cmd.execute()
    50.0
    """

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def execute(self):
        return self.price * self.quantity

# ApplyDiscountCommand
# This command applies a discount to a given revenue amount.

class ApplyDiscountCommand(Command):
    """
    Applies a discount to the revenue.

    Parameters:
    revenue (float): Original revenue.
    discount (float): Discount rate as a decimal (e.g., 0.1 for 10%).

    Examples:
    >>> discount_cmd = ApplyDiscountCommand(100.0, 0.1)
    >>> discount_cmd.execute()
    90.0
    """

    def __init__(self, revenue, discount):
        self.revenue = revenue
        self.discount = discount

    def execute(self):
        return self.revenue * (1 - self.discount)

# CalculateNetRevenueCommand
# This command calculates net revenue by applying a tax rate on the discounted revenue.

class CalculateNetRevenueCommand(Command):
    """
    Calculates net revenue after tax.

    Parameters:
    revenue (float): Revenue after discounts.
    tax_rate (float): Tax rate as a decimal (e.g., 0.2 for 20%).

    Examples:
    >>> net_revenue_cmd = CalculateNetRevenueCommand(90.0, 0.2)
    >>> net_revenue_cmd.execute()
    72.0
    """

    def __init__(self, revenue, tax_rate):
        self.revenue = revenue
        self.tax_rate = tax_rate

    def execute(self):
        return self.revenue * (1 - self.tax_rate)
#  Organize Commands Using the Command Pattern
# We'll create a RevenueCalculator context that uses these commands to calculate net revenue. This context runs the sequence of commands and would be tested using pytest for more complex scenarios.

class RevenueCalculator:
    def __init__(self, price, quantity, discount, tax_rate):
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.tax_rate = tax_rate

    def calculate_net_revenue(self):
        # Step 1: Calculate total revenue
        revenue_cmd = CalculateRevenueCommand(self.price, self.quantity)
        total_revenue = revenue_cmd.execute()

        # Step 2: Apply discount
        discount_cmd = ApplyDiscountCommand(total_revenue, self.discount)
        discounted_revenue = discount_cmd.execute()

        # Step 3: Calculate net revenue after tax
        net_revenue_cmd = CalculateNetRevenueCommand(discounted_revenue, self.tax_rate)
        net_revenue = net_revenue_cmd.execute()

        return net_revenue
# Step 3: Testing with Doctest and Pytest
# Using Doctests
# The doctests within each command class (e.g., CalculateRevenueCommand, ApplyDiscountCommand, and CalculateNetRevenueCommand) verify that each command behaves as expected in isolation. You can run doctests with the following command:

# Run in terminal 
# python -m doctest -v filename.py

# Add pytest
# For more complex testing scenarios, such as verifying the entire sequence of commands within RevenueCalculator, you can write tests in pytest.

# test_revenue_calculator.py
import pytest
from revenue_commands import RevenueCalculator

def test_calculate_net_revenue():
    calculator = RevenueCalculator(price=10.0, quantity=5, discount=0.1, tax_rate=0.2)
    net_revenue = calculator.calculate_net_revenue()
    assert net_revenue == 72.0  # Expected result based on calculations

#Run 
# pytest test_revenue_calculator.py