'''R-6.10 Consider what happens if the loop in the ArrayQueue. resize method at
lines 53–55 of Code Fragment 6.7 

for k in range(self._size):     # only consider existing elements
  self._data[k] = old[walk] # rather than old[walk] # intentionally shift indices
  walk = (1 + walk) % len(old)  # use old size as modulus
  

had been implemented as:


for k in range(self._size):
  self._data[k] = old[k] # rather than old[walk]
  
  
Give a clear explanation of what could go wrong.'''
