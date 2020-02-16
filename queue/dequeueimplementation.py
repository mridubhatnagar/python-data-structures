class Dequeue:
	"""
	Front is left side of list.
	Rear is right side of list.
	"""

	def __init__(self):
		self.items = []


	def addFront(self, item):
		"""
		Front is assumed to be start of list, i.e 0th position.
		Rear is assumed to be the end of list.
		"""
		self.items.insert(0, item)


	def addRear(self, item):
		"""
		Rear is end of the list. 
		"""
		self.items.append(item)


	def removeFront(self):
		"""
		Remove element from front.
		"""
		return self.items.pop(0)


	def removeRear(self):
		"""
		Remove element from rear
		"""
		return self.items.pop()


	def isEmpty(self):
		"""
		To check if the list is empty.
		"""
		if len(self.items) == 0:
			return True
		else:
			return False


	def size(self):
		"""
		To return the length of array.
		"""
		return len(self.items)

	def display(self):
		return self.items


dequeue = Dequeue()
dequeue.isEmpty()
dequeue.addRear(4)
dequeue.addRear('dog')
dequeue.addFront('cat')
dequeue.addFront(True)
dequeue.display()
dequeue.size()
dequeue.isEmpty()
dequeue.addRear(8.4)
dequeue.removeRear()
print(dequeue.display())