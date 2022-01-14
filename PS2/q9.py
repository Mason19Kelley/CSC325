# R-10.13 What is the worst-case time for putting n entries in an initially empty hash
# table, with collisions resolved by chaining? What is the best case?

#The worst case would occur whenever all entries have the same hash value (i.e. hash collisions exist for every entry).
#This means that there would be a linear search for any element n (O(n)) and then a check for duplicates (O(n)), making it
#O(n^2).

#The best case occurs whenever all entries have different hash values (i.e. no has collisions). Thus, every entry
#would take O(1) to enter and this is done n times. n * 1 = O(n).
