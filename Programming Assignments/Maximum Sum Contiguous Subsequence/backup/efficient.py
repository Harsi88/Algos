import random as r
import time
import pdb

# order n algorithm

n = 100000	   #Size of the list
m = 100    #Upper limit for elements in list a
l = -100   #lower limit for elements in list a
#f = open("randomList","w+b")  # file to write in
a = []

for i in range(0,n):
    a.append(r.randrange(l,m))


#a = [16, 13, -8, -96, -26, 0, -51, 27, 76, 10]
a = [-11, 35, 36, 40, 33, -1, 59, 77, 76, 22]
n = len(a)
s = -100000000000
si = sj = 0
msi = msj = 0
maxx = -1000000000000
t = time.time()

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
    
    print s,si,sj,maxx

tt = time.time() - t

print a
print maxx,msi,msj        
print tt*1000000
