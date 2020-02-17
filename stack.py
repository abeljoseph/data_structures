class stack_l:
	"""Stack implemented using a list."""
	def __init__(self):
		self.items = []

	def __repr__(self):
		return f"stack({str(self.items)})"

	def push(self,value):
		self.items.append(value)

	def pop(self):
		popped_item = self.items[-1]
		self.items = self.items[:-1]
		return popped_item

	def peek(self):
		return self.items[-1]


class Node:
	"""General node for linked list implementation."""
	def __init__(self, data=None):
		self.data = data
		self.next = None

