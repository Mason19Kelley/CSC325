#Implement "reverse" as a method of _DoublyLinkedBased, called as L.reverse(),
# that reverses the _DoublyLinkedBase instance L, yet without creating or destroying any nodes.
from random import randint



class _DoublyLinkedBase:
	class _Node:

		def __init__(self, element=None, prev=None, next=None):
			self.element = element
			self.next = next
			self.prev = prev

		def __str__(self):
			return str(self.element)

	def __init__(self):
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header.next = self._trailer
		self._trailer.prev = self._header
		self._size = 0


	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def insert_between(self, e, pred, succ):
		newest = self._Node(e, pred, succ)
		pred.next = newest
		succ.prev = newest
		self._size += 1
		return newest

	def delete_node(self, node):
		predecessor = node.prev
		successor = node.next
		predecessor.next = successor
		successor.prev = predecessor
		self._size -= 1
		element = node.element  # record deleted element
		node.prev = node.next = node.element = None  # deprecate node
		return element

	def prepend(self, value):
		self.insert_between(value, self._header, self._header.next)


	def reverse(self):
		temp = self._header.next
		while temp.element != None:
			temp.next, temp.prev = temp.prev, temp.next
			temp = temp.prev
		self._header.next, self._header.prev = None, self._header.next
		self._trailer.next, self._trailer.prev = self._trailer.prev, None
		self._trailer, self._header = self._header, self._trailer

	def __str__(self):
		temp = self._header
		s = ""
		while temp != None:
			s += f"{temp}-"
			temp = temp.next
		return s

if __name__ == "__main__":
	L = _DoublyLinkedBase()
	for i in range(10):
		L.prepend(randint(0,10))
	print(L)
	L.reverse()
	print(L)

