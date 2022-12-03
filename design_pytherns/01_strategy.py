#  you have a SupportTicket class as well as a CustomerSupport class at the top
# while has a concrete method called generate_id for all Support tickets
# CustomerSupport tend to have different strategies to get to no more tickets left
# can go Lifo, fifo, random, etc... All these are separate methods with their own defs
# inside CustomerSupport we have a 
# plural: def process_tickets(self, ordering: Callable[[List[SupportTicket]], List[SupportTicket]]):
# that one iterates through the tickets and can be called by passing as an argument one of the separate methods
# like app.process_tickets(fifoOrdering)
# you can now create a new_processing_tickets_method and def it independantly. The code is ready for it and you just
# call it through app.process_tickets(new_processing_tickets_method)
# This a more functional approach to the strategy pattern. You could also use a syntax with abstract classes but it is more 
# verbose.

import string
import random
from typing import List, Callable # this Callable keyword makes the process more strict, ie we expect to see functions
#  being passed... Callable is a function-like object. Either a function or a class that behaves like a function
# typical typo I do, to avoid, it is written Callable not Calleable!


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifoOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    return list.copy()


def filoOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def randomOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


def blackHoleOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    return []


class CustomerSupport:

    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

# below is a key code block for callable that get a List of Support Tickets and return also a lost of support tickets
    def process_tickets(self, ordering: Callable[[List[SupportTicket]], List[SupportTicket]]):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(blackHoleOrdering)