#Implement a recursive Python function with the signature clear(S) for removing all the elements from an ArrayStack S.


class ArrayStack:

	def __init__(self):
		self.data = []

	def __len__(self):
		return len(self.data)

	def is_empty(self):
		return len(self.data) == 0

	def push(self, e):
		self.data.append(e)

	def top(self):
		if self.is_empty():
			raise Empty("Stack is empty.")
		return self.data[-1]

	def pop(self):
		if self.is_empty():
			raise Empty("Stack is empty.")
		return self.data.pop()

def clear(S):
	if len(S) == 0:
		return
	else:
		S.pop()
		return clear(S)

S = ArrayStack()
for i in range(10):
	S.push(i)

for i in range(10):
	print(S.data)
	S.pop()
