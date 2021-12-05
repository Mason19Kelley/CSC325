#Implement "reverse" as a method of _DoublyLinkedBased, called as L.reverse(),
# that reverses the _DoublyLinkedBase instance L, yet without creating or destroying any nodes.



class _DoublyLinkedBase:
	class _Node:

		def __init__(self, element=None, next=None, prev=None):
			self.element = element
			self.next = next
			self.prev = prev

		# def getElement(self):
		# 	return self._element
		#
		# def getNext(self):
		# 	return self._next
		#
		# def setElement(self, newElem):
		# 	self._element = newElem
		#
		# def setNext(self, newNext):
		# 	self._next = newNext

	def __init__(self):
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header.next = self._trailer
		self._trailer.prev = self._header
		self._size = 0


	def __len__(self):
		return self._size