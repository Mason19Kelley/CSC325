from time import time
 
def example1(S): # O(n)
    n = len(S)
    total = 0
    for j in range(n): # T(n) = n
        total += S[j]
    return total
 
def example2(S): # O(n)
    n = len(S)
    total = 0
    for j in range(0, n, 2): # T(n) = n/2
        total += S[j]
    return total
 
def example3(S): # O(n^2)
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1 + j):
            total += S[k]
    return total
 
def example4(S): # O(n)
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):  # T(n) = n
        prefix += S[j]
        total += prefix
    return total

if __name__ == "__main__":
	"""
	The following code will run a single function.
	Repeat similar codes for all four functions.
	Make sure to use the same input for each function execution.
	Execute multiple runs with different sizes of input.
	"""
	start_time = time()
	S = range(10)
	example1(S)
	end_time = time()
	T_time = end_time - start_time
	print("Execution time = {}".format(T_time))
