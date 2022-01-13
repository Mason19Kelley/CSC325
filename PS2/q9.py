# R-10.13 What is the worst-case time for putting n entries in an initially empty hash
# table, with collisions resolved by chaining? What is the best case?


The worst case would occur whenever all entries have the same hash value (i.e. hash collisions exist for every entry).
This means that there would be a linear search for any element n (O(n)) and then a check for duplicates (O(n)), making it
O(n^2).

The best case occurs whenever all entries have different hash values (i.e. no has collisions). This would make it O(n).






# Worst case for adding n entries is gonna be O(n^2) if every single entry
# goes into the exact same hash location. This is because insertion into a linked list
# takes O(n) when inserting to the end. n entries inserted with a time complexity of O(n)
#  = n * n = O(n^2)

# Best case for adding n entries is going to have a time complexity of O(n). This is the case
# where each entry goes into the hash without duplicate hash keys. Thus, each entry
# would take O(1) to enter and this is done n times. Thus, n * 1 = O(n).

