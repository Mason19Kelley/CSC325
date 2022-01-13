 #Implement the in-place heap-sort algorithm and experimentally determine its 
 #running time (using a similar approach as in the first assignment).

arr = [1,7,43,90,4,6]
# Turns an array into a max heap by working from the bottom up with each sub-heap
def heapify(Arr, Arr_len, i):
	# set indixes for current subheap
	larg = i
	l_ind = 2*i+1
	r_ind = 2*i+2

	# find largest value
	if l_ind < Arr_len and A[l_ind] > A[larg]:
		larg = l_ind

	if l_ind < Arr_len and A[l_ind] > A[larg]:
		larg = r_ind

	if larg != i:
		Arr[i], Arr[larg] = Arr[larg], Arr[i]
		# run heapify again to find largest node between the 3
		heapify(Arr , Arr_len, larg)




# turn a Max-heap into a sorted array
def heapSort(Arr):