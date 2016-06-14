import harsimran
import random
import numpy
import time


def mat(k,m1,m2,n):
    a = []
    for k in range(k):
        sample = [0]*m1
        for i in range(m1):
            temp = []
            for j in range(m2):
                temp.append(random.randrange(1,n))
            sample[i] = temp
        a.append(sample)
    return a

def blast(k,m1,m2,n):
    """
    k = number of iterations to perform
    m1 X m2 = size of square matrix
    n = number of colors + 1
    """   
    a,s = mat(k,m1,m2,n),[]
    for i in range(len(a)):
        t = time.time()
        l = harsimran.solve(numpy.matrix(a[i]))
        t = time.time()-t
        print l[-1],t
        s.append(l[-1])
    print "avg:",sum(s)/k

