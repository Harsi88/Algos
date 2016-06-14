import random as r

# order n^2 algorithm

def algo(a):
    """
    This is better algorithm than brute force for finding Maximum Sum Contiguous
    Sub-sequence.
    Its Time-complexity is order of N^2
    """
    n = len(a)
    s = -100000000000000000
    si = sj = 0
    addresultij = 0

    for i in range(0,n):
        addresultij = a[i]
        for j in range(i,n):
            if i!=j:
                addresultij += a[j]
            if s<=addresultij:
                s = addresultij
                si = i
                sj = j

    return [s,si,sj]
