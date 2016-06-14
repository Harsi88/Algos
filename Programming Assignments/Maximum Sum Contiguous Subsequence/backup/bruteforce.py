import random as r
import time

# order n^3 (nC2 * n) algorithm

def add(a,i,j):
    s = 0
    for k in range(i,j):
        s += a[k]
    return s


n = 2000	   #Size of the list
m = 100    #Upper limit for elements in list a
l = -100   #lower limit for elements in list a
#f = open("randomList","w+b")  # file to write in
a = []

for i in range(0,n):
    a.append(r.randrange(l,m))


#a = [16, 13, -8, -96, -26, 0, -51, 27, 76, 10]
n = len(a)
s = -100000000000000000
si = sj = 0

t = time.time()

for i in range(0,n):
    for j in range(i+1,n+1):
        temp = add(a,i,j)
        if s<=temp:
            s = temp
            si = i
            sj = j-1

tt = time.time() - t

#print a
print s,si,sj        
print tt*1000000
