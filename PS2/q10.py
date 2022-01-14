# Draw an example skip list S that results from performing the following
# series of operations on the skip list shown in Figure 10.13: del S[38],
# S[48] = x , S[24] = y , del S[55]. Record your coin flips, as well.

# -inf------------------------------------------inf
# -inf------17----------------------------------inf
# -inf------17------------------42----------55--inf
# -inf------17------31----------42----------55--inf
# -inf--12--17------31--38------42--44------55--inf
# -inf--12--17--20--31--38--39--42--44--50--55--inf

# del S[38], first we must navigate to 38 in the bottom list.
# Next we must work our way up to the max height of 38 deleting the number as we go and
# setting links from left neighbor to right neighbor as we go. This will result in:

# -inf--------------------------------------inf
# -inf------17------------------------------inf
# -inf------17--------------42----------55--inf
# -inf------17------31------42----------55--inf
# -inf--12--17------31------42--44------55--inf
# -inf--12--17--20--31--39--42--44--50--55--inf

# S[48] = x, Insert x into 48. 48 is not found, so we insert 48 with a sequence of (insert, heads, tails)
# -inf------------------------------------------inf
# -inf------17----------------------------------inf
# -inf------17--------------42--------------55--inf
# -inf------17------31------42--------------55--inf
# -inf--12--17------31------42--44--48------55--inf
# -inf--12--17--20--31--39--42--44--48--50--55--inf


# S[24] = y, Insert y into 24. 24 is not found, so we insert 24 with a sequence of (insert, tails)
# -inf----------------------------------------------inf
# -inf------17--------------------------------------inf
# -inf------17------------------42--------------55--inf
# -inf------17----------31------42--------------55--inf
# -inf--12--17----------31------42--44--48------55--inf
# -inf--12--17--20--24--31--39--42--44--48--50--55--inf

# del S[55], first we must navigate to 38 in the bottom list.
# Next we must work our way up to the max height of 55 deleting the number as we go and
# setting links from left neighbor to right neighbor as we go. This will result in:

# -inf------------------------------------------inf
# -inf------17----------------------------------inf
# -inf------17------------------42--------------inf
# -inf------17----------31------42--------------inf
# -inf--12--17----------31------42--44--48------inf
# -inf--12--17--20--24--31--39--42--44--48--50--inf