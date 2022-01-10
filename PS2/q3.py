# Give an example of a worst-case sequence with n elements for insertion-
# sort, and show that insertion-sort runs in Ω(n2) time on such a sequence.


# The worst case scenario for insertion sort is going to occur when the list is in decreasing order.
# An example is [9,8,7,6,5,4,3,2,1,0]
# Insertion sort builds a "sorted" and "unsorted" list out of the same array throuch comparisons and swaps.
# For the first iteration, the algorithm performs 0 comparisons.
# For iteration 2, only 1 comparisons and swaps is performed between the first 2 elements to see which is smaller.
# this continues for the whole list where each iteration increases until n-1 comparisons and swaps are performed for the last element.
# A summation for total number of comparisons and swaps for this case is
# Σ(from i=1 to N) (i-1) which equals (n^2 - n)/2
# Thus, the runtime of this algorithm is always n^2.
