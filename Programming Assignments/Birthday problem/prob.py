import random

for n in range(1,101):
    prob = 0
    for j in range(0,1000):
        a = []
        for i in range(1,n):
            a.append(random.randrange(1,365))

	a.sort()
	
	for i in range(0,n-2):
	    if(a[i]==a[i+1]):
	        prob+=1
	        break
	        
    result = prob*1.0/1000
    print n,result
