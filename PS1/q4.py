#show the summation of log(i) for i=1 to N is Ω(nlog(n)) 
Σ(from i=1 to N) (log(i)) = log(1)+log(2)+...+log(N)
>= Σ(from i=1 to N/2) log(i)
>= n/2 log(n/2)
>= n/4 log(n) for n>=4
therefore Σ(from i=1 to N) log(i) = Ω(nlog(n))
