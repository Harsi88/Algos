import random as r
import time
import pdb

# order n algorithm

def max_subseq(a,m,n):
    if m==n:
       return [a[m],m,n]
    aa = max_subseq(a,m,int(m+n)/2)
    bb = max_subseq(a,int(m+n)/2+1,n)
    print aa,bb
    if aa==None:
        return bb
    if bb==None:
        return aa
    if (aa[2]+1)!=int(m+n)/2 and bb[1]!=int(m+n)/2+1:
        if aa[0]>bb[0]:
            return aa
        else:
            return bb
    else:
        if aa[0]>bb[0]:
            if aa[0]>(aa[0]+bb[0]):
                return aa
            else:
                return [sum(a[aa[1]:bb[2]+1]),aa[1],bb[2]]
        else:
            if bb[0]>(aa[0]+bb[0]):
                return bb
            else:
                return [sum(a[aa[1]:bb[2]+1]),aa[1],bb[2]]
    
n = 10	   #Size of the list
m = 100    #Upper limit for elements in list a
l = -100   #lower limit for elements in list a
#f = open("randomList","w+b")  # file to write in
a = []

for i in range(0,n):
    a.append(r.randrange(l,m))


#a = [16, 13, -8, -96, -26, 0, -51, 27, 76, 10]
a = [-11, 35, 36, 40, 33, -1, 59, 77, 76, 22]
n = len(a)

t = time.time()

m = max_subseq(a,0,n-1)
#m[0] = sum(a[m[1]:m[2]+1])

tt = time.time() - t

print a
print m        
print tt*1000000
