import random
import matplotlib.pyplot as plt

data = []
b = []
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
    data.append(result)
    
for i in range(1,101):
    b.append(i)
    
plt.plot(b,data,'ro')
plt.title("Birthday Problem")
plt.xlabel("Number of persons chosen at random")
plt.ylabel("Probability of birthday collisions")	
plt.show()
