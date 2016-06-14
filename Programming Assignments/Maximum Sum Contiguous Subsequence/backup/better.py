import random as r
import time

# order n^2 algorithm

n = 1000	   #Size of the list
m = 100    #Upper limit for elements in list a
l = -100   #lower limit for elements in list a
#f = open("randomList","w+b")  # file to write in
a = []

for i in range(0,n):
    a.append(r.randrange(l,m))


a = [49, -86, -90, 44, -97, -31, 31, -73, 37, 2]
n = len(a)
s = -100000000000000000
si = sj = 0
addresultij = 0

t = time.time()

for i in range(0,n):
    addresultij = a[i]
    for j in range(i,n):
        if i!=j:
            addresultij += a[j]
        if s<=addresultij:
            s = addresultij
            si = i
            sj = j

tt = time.time() - t

print a
print s,si,sj        
print tt*1000000
