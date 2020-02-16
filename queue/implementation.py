class Queue:

	def __init__(self):
		self.list = []


	def enqueue(self, item):
		"""
		Inserts an element in a queue.
		"""
		return self.list.append(item)

	
	def dequeue(self):
		"""
		Removes an element from a queue.
		"""
		return self.list.pop(0)


	def isEmpty(self):
		"""
		Checks if the queue is empty.
		"""
		if len(self.list) == 0:
			return True
		else:
			return False


	def size(self):
		"""
		Size of the queue
		"""
		return len(self.list)

	def display(self):
		"""
		Display the list.
		"""
		return self.list	



queue = Queue()
queue.isEmpty()
queue.enqueue(4)
queue.enqueue('dog')
queue.enqueue(True)
queue.size()
queue.isEmpty()
queue.enqueue(8.4)
queue.dequeue()
queue.dequeue()
queue.size()
print(queue.display())