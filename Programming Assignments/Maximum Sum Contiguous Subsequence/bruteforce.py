import random as r

# order n^3 (nC2 * n) algorithm

def add(a,i,j):
    """
    Add function gives you the sum of elements in list a
    from index i to j
    """
    s = 0
    for k in range(i,j):
        s += a[k]
    return s

def algo(a):
    """
    This is brute force algorithm for finding Maximum Sum Contiguous
    Sub-sequence.
    Its Time-complexity is order of N^3
    """
    n = len(a)
    s = -100000000000000000
    si = sj = 0

    for i in range(0,n):
        for j in range(i+1,n+1):
            temp = add(a,i,j)
            if s<=temp:
                s = temp
                si = i
                sj = j-1

    return [s,si,sj]
