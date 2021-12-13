#Show that the summation of i^2 from i=1 to N is O(n^3)
Σ(from i=1 to N) (i^2)
Σ(from i=1 to N) (i^2) <= Σ(from i=1 to N) (N^2) since i is always less than or equal to N.
An example summation would look like:
Σ(from i=1 to N) (N^2)
Since N^2 is a factor of every term in the summation, we can factor it out.
N^2(Σ(from i=1 to N) (1))
The 2nd factor in this product is equal to N because it is adding 1 N times.
This leaves us with (N^2)*N which is O(N^3).