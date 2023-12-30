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

        def push(self, value):
		if self.head.data == None:  # stack is empty
			self.head.data = value
			return


		lastNode = self.head
		while lastNode.next != None:
			lastNode = lastNode.next

		# Create a new Node to hold the pushed data
		lastNode.next = Npde()
		lastNode.next.data = value

	def pop(self):
		# Case 1: list size is 0
		if self.head.data == None: raise IndexError("Cannot pop from empty stack.")
		# Case 2: list size is 1
		if self.head.next == None:
			value = self.head.data
			self.head.data = None
			return value

		# Case 3: list size is greater than 1
		lastNode = self.head
		while lastNode.next.next != None:
			lastNode = lastNode.next

		value = lastNode.next.data
		lastNode.next = None
		return value

	def peek(self):
		# Case 1: list size is 0
		if self.head.data == None: raise IndexError("Cannto peek from empty stack.")
		# Case 2: list size is 1
		if self.head.next == None:
			return self.head.data

		# Case 3: list size is greater than 1
		lastNode = self.head
		while lastNode.next.next != None:
			lastNode = lastNode.next

		return lastNode.next.data
