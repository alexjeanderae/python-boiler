# Strategy pattern
# 
# In short, Strategy is about choosing an algorithm at runtime, while Command is about creating self-contained actions that can be triggered or queued independently. For example, you have data that you need to process, you can imagine three ordering strategies: FIFO (First-In-First-Out), FILO (First-In-Last-Out), Random, etc.. These will be decided at Run time .
#
# Another example would be to define for instance three difference actions upon receiving an API response from a Weather app.

# Wach API response triggers a specific strategy at runtime. For example, you might use a function that interprets the response and then chooses the appropriate strategy. 

from typing import List, Callable

# Weather warning types as strategy functions
def no_warning(contact_list: List[str], postcodes: List[str]):
    print("API Response: No Warning")
    print("No action needed.")

def mild_warning(contact_list: List[str], postcodes: List[str]):
    print("API Response: Mild Warning")
    print("Notifying affected contacts for a mild warning.")
    for contact in contact_list:
        print(f"Sending mild warning to {contact}")

def severe_warning(contact_list: List[str], postcodes: List[str]):
    print("API Response: Severe Warning")
    print("High-priority alert for all contacts in affected areas.")
    for contact in contact_list:
        print(f"Sending SEVERE warning to {contact} in areas: {', '.join(postcodes)}")

# WeatherAlertSystem with strategy selection based on API response
class WeatherAlertSystem:
    def __init__(self):
        self.contacts = ["Alice", "Bob", "Charlie"]  # Contacts to notify

    def process_warning(self, warning_strategy: Callable[[List[str], List[str]], None], postcodes: List[str]):
        warning_strategy(self.contacts, postcodes)

# Function to interpret API response and choose a strategy
def handle_api_response(alert_system, api_response: str, postcodes: List[str]):
    if api_response == "No Warning":
        alert_system.process_warning(no_warning, postcodes)
    elif api_response == "Mild Warning":
        alert_system.process_warning(mild_warning, postcodes)
    elif api_response == "Severe Warning":
        alert_system.process_warning(severe_warning, postcodes)
    else:
        print("Unknown warning level received from API.")

# Example usage simulating API responses
alert_system = WeatherAlertSystem()

print("Example 1: API Response -> No Warning")
handle_api_response(alert_system, "No Warning", [])

print("\nExample 2: API Response -> Mild Warning")
handle_api_response(alert_system, "Mild Warning", ["1010", "2020"])

print("\nExample 3: API Response -> Severe Warning")
handle_api_response(alert_system, "Severe Warning", ["1010", "2020", "3030"])
