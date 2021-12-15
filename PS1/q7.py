'''R-6.10 Consider what happens if the loop in the ArrayQueue. resize method at
lines 53–55 of Code Fragment 6.7 

for k in range(self._size):     # only consider existing elements
  self._data[k] = old[walk] # rather than old[walk] # intentionally shift indices
  walk = (1 + walk) % len(old)  # use old size as modulus
  

had been implemented as:


for k in range(self._size):
  self._data[k] = old[k] # rather than old[walk]
  
  
Give a clear explanation of what could go wrong.'''

'''
in the updated code, self._data copies the data from the queue old at index k, storing it at index k. the problem with this is that k begins at 0,
and this may not be the first index of the queue. this would only work if the queue old were not wrapped around; however, if it were, the second half
of the queue — that which is wrapped around to the front — would be copied first, causing the elements of the queue to be copied in the incorrect order.
'''
