#Implement a recursive Python function with the signature clear(S) for removing all the elements from an ArrayStack S.


def clear(S):
	if len(S) == 0:
		return
	else:
		S.pop()
		return clear(S)
