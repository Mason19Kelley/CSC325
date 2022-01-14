#Define the internal path length, I(T), of a tree T to be the sum of the
#depths of all the internal positions in T. Likewise, define the external path
#length, E(T), of a tree T to be the sum of the depths of all the external
#positions in T. Show that if T is a proper binary tree with n positions, then
#E(T) = I(T) +n−1.

'''
Base case a tree has one node n = 1. E(T) = 0 and I(T) = 0 => E(T) = I(T) + n - 1 = 0
Induction Step: 
Assume that any proper binary tree with n nodes >= 1 satisfies E(T) = I(T) + n - 1 
then n+1 also holds true.
Assume that the length of an internal node p has a maximum depth of d meaning that it has two external
children with depths d + 1. Remove the two external nodes we get the number of nodes n = n+1 -2 = n-1 
which leads to the equation E(T') = I(T') + (n-1) - 1 
two external nodes (2(h+1)) were removed making the parent of those nodes an external node (h) 
Hence, E(T') = E(T) - 2(h+1)+h 
Therefore by induction hypothesis, E(T) - h - 2 = I(T) - h + n - 3 => E(T) = I(T) + n - 1
'''
