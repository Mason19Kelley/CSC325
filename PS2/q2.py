#Define the internal path length, I(T), of a tree T to be the sum of the
#depths of all the internal positions in T. Likewise, define the external path
#length, E(T), of a tree T to be the sum of the depths of all the external
#positions in T. Show that if T is a proper binary tree with n positions, then
#E(T) = I(T) +n−1.

'''
Basis:
  A tree has one node n = 1, so E(T) = 0 and I(T) = 0 => Since n = 1, n - 1 = 0, so E(T) = I(T) + n - 1 = 0
Induction Step: 
  Assume that any proper binary tree with nodes n >= 1 satisfies E(T) = I(T) + n - 1. Prove true for a binary tree with
  nodes n+1.
  Assume that the length of an internal node p has a maximum depth of d, meaning that it has two external
  children with depths d + 1. Remove the two external nodes and the tree now has nodes n = n+1-2 = n-1,
  so E(T') = I(T') + (n-1) - 1. Because two external nodes (2(d+1)) were removed, making the parent of those nodes an external node (d), 
  E(T') = E(T) - 2(d+1)+d; I(T') = I(T) - d. Therefore, by the induction hypothesis, E(T) - d - 2 = I(T) - d + n - 3  = 0 => E(T) = I(T) + n - 1 is true for every
  proper biary tree with n+1 nodes.
'''
