import random
import pdb
import Gnuplot
n=1000
count=[]
for y in range(0,n):
	count.append(0)

for z in range(0,1000):
	rank=[]

	"""rank stores the quality of assistants coming for interview"""

	for x in range(0,n):
		rank.append(random.random())

	if (rank.index(max(rank))==0):
		count[0]+=1		
		
	for k in range(1,n):
	
#	""" here k denotes first k assistants that are rejected"""

		m=max(rank[0:k])
		i=k

		while m > rank[i] and i<n-1:
			i+=1
	
		if i==(rank.index(max(rank))):
			count[k]+=1





l=[]
for z in range(0,n):
	t=[]
	t.append(z)
	t.append(count[z]/10000.0)
	l.append(t)

g=Gnuplot.Gnuplot(persist=True)
g.xlabel("Number of rejections before selecting a candidate")
g.ylabel("Probability")
g('setxrange[0,n]')
g('setyrange[0,1]')
g.plot(l)




	


