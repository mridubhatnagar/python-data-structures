"""
Stack:
1. Ordered collection of items in which addition and removal takes place from same end.
2. Operations
- Stack()
- push(item)
- pop()
- peek()
- isempty()
- size()

"""

class Stack:

	def __init__(self):
		self.list = []


	def push(self, item):
		"""
		Inserts an item in stack.
		"""
		self.list.append(item)

	def pop(self):
		"""
		Removes an item from the stack.
		"""
		return self.list.pop()

	def peek(self):
		"""
		Only shows the top element. Does not
		remove element from list.
		"""
		return self.list[len(self.list) - 1]

	def isempty(self):
		"""
		Checks if list is empty or not.
		"""
		if len(self.list)==0:
			return True
		else:
			return False

	def size(self):
		"""
		Checks the size of list.
		"""
		return len(self.list)

	def showcontent(self):
		"""
		Show stack.
		"""
		return self.list


"""
Testing 

s = Stack()
print(s.isempty())
s.push(4)
print(s.showcontent())
s.push('dog')
print(s.peek())
s.push(True)
print(s.showcontent())
s.size()
s.isempty()
s.push(8.4)
s.pop()
s.isempty()
s.size()
print(s.showcontent())
"""