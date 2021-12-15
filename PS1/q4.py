# show the summation of log(i) for i=1 to N is Ω(nlog(n)) 
Σ(from i=1 to N) (log(i)) = log(1) + log(2) + ... log (n/2) + ... + log(N)
>= 0 * log(1) + 0 * log(2) + ... log(n/2) + ... + log(N)
>= n/2 log(n/2)
# division of logs, so:
= n/2 (log(n) - log(2))
= n/2 (log(n) - 1)
= (n/2)(log(n)) - (n/2)
# thus, Σ(from i=1 to N) (log(i)) = Ω(nlog(n))
