import random as r

def algo(a):
    """
    This is the most efficient algorithm for finding Maximun
    Contiguous Sub-sequence, running in order N time.
    """
    n = len(a)
    s = -100000000000      #stores maximum sum of sub-sequence betweem indices si and sj
    si = sj = 0
    msi = msj = 0	   #stores indices corresponding to maximum sum sub-sequence till index k
    maxx = -1000000000000  #stores maximum sum of sub-sequence till index k

    for k in range(0,n):
        if s > 0:
            s = s + a[k]
            si = si
            sj = k
            if maxx < s:
                maxx = s
                msi = si
                msj = sj
        else:
            s = a[k]
            si = k
            sj = k
            if maxx < s:
                maxx = s
                msi = si
                msj = sj
    
    return [maxx,msi,msj]
