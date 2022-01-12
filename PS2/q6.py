#Give a nonrecursive implementation of the downheap method for the class HeapPriorityQueue.
def _downheap(self, j):
	# to continue the process without recursion,
	# a while loop with the following condition can be constructed:
	while self._has_left(j):
		# the recursive call would fail if this condition
		# were not met in the original if statement
		left = self._left(j)
		small_child = _left
		if self._has_right(j):
			right = self._right(j)
			if self._data[right] < self._data[left]:
				small_child = right
			if self._data[small_child] < self._data[j]:
				# swaps j and small_child
				self._swap(j, small_child)
				# gets rid of j
				j = small_child
			else:
				break
