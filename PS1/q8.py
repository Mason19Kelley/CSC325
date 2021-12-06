#Implement "reverse" as a method of SinglyLinkedList, called as L.reverse(),
# that reverses the SinglyLinkedList instance L
# using only a constant amount of additional space and not using any recursion.


class SinglyLinkedList:
	class _Node:
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def add_first(self, e):
		self._head = self._Node(e, self._head)
		if self.is_empty():
			self._tail = self._head
		self._size += 1

	def add_last(self, e):
		newnode = self._Node(e, None)
		if self.is_empty():
			self._head = newnode
		else:
			self._tail._next = newnode
		self._tail = newnode
		self._size += 1

	def remove_first(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return answer

	def remove_last(self):
		if self.is_empty():
			raise Empty('Linked list is empty')
		if self._size == 1:
			answer = self._head._element
			self._head = None
			self._tail = None
		else:
			answer = self._tail._element
			current_node = self._head
			next_node = current_node._next
			while next_node != self._tail:
				current_node = next_node
				next_node = next_node._next
			self._tail = current_node
		self._size -= 1
		return answer
