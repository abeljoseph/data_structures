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


class stack_ll:
	"""Stack implemented using a linked list."""
	def __init__(self):
		self.head = Node()

	def __repr__(self):
		if self.head.data == None: return "stack{[]}"
		stack = [self.head.data]  # list to hold values
		lastNode = self.head

		while lastNode.next != None:
			lastNode = lastNode.next
			stack.append(lastNode.data)

			return f"stack({str(stack)})"

