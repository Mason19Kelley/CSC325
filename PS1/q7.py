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
if the method self.is_empty() were executed, self._front would be incremented by 1. given that self._front is initialized as 0 in the constructor
and self._front = (self._front + 1) % len(self._data) in this resizing method, self._front would become (0+1) % len(self._data), or 1. 
in this case, at lines 53-55, one the first run-through of this for loop, k = 0 and self._data[k] = old[1]; however, in the modified code, for k = 0,
self._data[k] = old[k], or self._data[0] = old[0]. this is simply the incorrect index associated with the desired element to be added to self._data from old.
'''
