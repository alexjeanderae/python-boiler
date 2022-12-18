# adapted from https://www.geeksforgeeks.org/command-method-python-design-patterns/


"""Use built-in abc to implement Abstract classes and methods"""
from abc import ABC, abstractmethod

"""Class Dedicated to Command"""
class Command(ABC):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver
	
	"""process method - is an abstract method - could add the decorator @abstractmethod"""
	def process(self):
		pass
	
	"""unprocess method - is an abstract method - could add the decorator @abstractmethod"""
	def unprocess(self):
		pass

"""Class dedicated to Command Implementation - should typically have one to a few of these, it further delegates some of the work to the receiver to be able to do complex things"""
class CommandImplementation(Command):
	
	"""constructor method"""
	def __init__(self, receiver):
		self.receiver = receiver

	"""process method"""
	def process(self):
		self.receiver.perform_action()
	
	"""unprocess method"""
	def unprocess(self):
		self.receiver.undo_action()

"""Class dedicated to Receiver - they carry the request and typically the core of the business logic"""
class Receiver:
	
	"""perform-action method"""
	def perform_action(self):
		print('Action performed in receiver.')
	
	"""undo-action method"""
	def undo_action(self):
		print('Action undone in receiver.')

"""Class dedicated to Invoker - could add get, set, instantiation logic here"""
class Invoker:
	
	"""command method"""
	def command(self, cmd):
		self.cmd = cmd

	"""execute method"""
	def execute(self):
		self.cmd.process()
	
	"""unexecute method"""
	def unexecute(self):
		self.cmd.unprocess()

"""main method"""
if __name__ == "__main__":
	
	"""create Receiver object"""
	receiver = Receiver()
	cmd = CommandImplementation(receiver)
	invoker = Invoker()
	invoker.command(cmd)
	invoker.execute()
	invoker.unexecute()
