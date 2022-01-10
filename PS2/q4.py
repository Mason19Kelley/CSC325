# R-10.9 Draw the 11-entry hash table that results from using the hash function,
# h(i)=(3i+5) mod 11, to hash the keys 12, 44, 13, 88, 23, 94, 11, 39, 20,
# 16, and 5, assuming collisions are handled by chaining.
#
# R-10.10 What is the result of the previous exercise, assuming collisions are handled
# by linear probing?
#
# R-10.11 Show the result of Exercise R-10.9, assuming collisions are handled by
# quadratic probing, up to the point where the method fails.
#
#
# R-10.12 What is the result of Exercise R-10.9 when collisions are handled by double
# hashing using the secondary hash function h(k) = 7−(k mod 7)?

# 10.9 [0[13],1[94->39],2[],3[],4[],5[44->88->11],6[],7[],8[12->23],9[16->5],10[20]]
# Above, the indexes are given before the element for ease of use.

# 10.10 [0[13],1[94],2[39],3[16],4[5],5[44],6[88],7[11],8[12],9[23],10[20]]
# Above, the indexes are given before the element for ease of use.

# 10.11 [0[13],1[94],2[39],3[11],4[],5[44],6[88],7[16],8[12],9[23],10[20]]
# Above, the indexes are given before the element for ease of use.
# Fails when trying to insert the last element.

# 10.12 # 10.10 [0[13],1[94],2[23],3[88],4[39],5[44],6[11],7[5],8[12],9[16],10[20]]
# # Above, the indexes are given before the element for ease of use.