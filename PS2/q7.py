 #Implement the in-place heap-sort algorithm and experimentally determine its 
 #running time (using a similar approach as in the first assignment).

arr = [-1, -7, -5, -3, -4]
# Turns an array into a max heap by working from the bottom up with each sub-heap
def heapify(Arr, Arr_len, i):
	# set indixes for current subheap
	larg = i
	l_ind = 2*i+1
	r_ind = 2*i+2

	# find largest value
	if l_ind < Arr_len and Arr[l_ind] > Arr[larg]:
		larg = l_ind

	if r_ind < Arr_len and Arr[r_ind] > Arr[larg]:
		larg = r_ind

	if larg != i:
		Arr[i], Arr[larg] = Arr[larg], Arr[i]
		# run heapify again to find largest node between the 3
		heapify(Arr , Arr_len, larg)




# turn a Max-heap into a sorted array
# O(nlog(n))
def heapSort(Arr):

	Arr_len = len(Arr)

	# We must start with the far right-most, lowest internal node
	# There is no point in looping through the external nodes as they have no children
	j = (Arr_len - 2) // 2
	# this loop will heapify each subheap starting from the 2nd lowest level
	# This will push the largest nums to the top
	for i in range(Arr_len - 1 , -1, -1):
		heapify(Arr, Arr_len, i)

	# Since this is a maxheap, we know the highest value is at Arr[0]
	# Thus, we can swap the max value to the end of the heap, filter it out
	# Then re-heapify the heap to get the next max value.
	for i in range(Arr_len - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)

print(arr)
heapSort(arr)
print(arr)
