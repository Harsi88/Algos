import random

class student:
    def __init__(self):
        self.prList = []
        self.pairweight = []
        self.pairs = []
        self.enum = ""
        self.name = ""
        self.ispair = False
        self.pair = 0
        
    def Id(self,nm,en):
        self.name = nm
        self.enum = en    
        
    def make(self,x,j):
        for i in range(0,len(x)-2):
            t = x[j].prList[i]
            b = []
#            print t 
#            print x[t].prList 
            b.append(i+x[t].prList.index(j))
            a = []
            a.append(j)
            a.append(t)
            b.append(a)
            self.pairweight.append(b)
            

f = open("pref.csv","rw+")


line = f.next()
line = f.next()
line = f.next()
line = f.next()

mapp = {}
rmapp = {}
c = 1
for j in range(1,41):
    line = f.next()
    fields = line.split(',')
    for i in fields:
        if len(i)<3:
           continue
        mapp[i.strip().upper()] = c
        rmapp[c] = i.strip().upper()
        c+=1
        break

x = []
x.append(student())

f.seek(0)

line = f.next()
line = f.next()
line = f.next()
line = f.next()


for j in range(1,41):
    line = f.next()
    fields = line.split(',')
    x.append(student())
    ct = 1
    for i in fields:
        if len(i)<3:
            continue
        if ct==1:
            x[j].enum = i
            ct+=1
            continue
        if ct==2:
            x[j].name = i
            ct+=1
            continue
        x[j].prList.append(mapp[i.strip().upper()])
        ct+=1
    
    p = 1
    while ct!=42:
        if  not p in x[j].prList:
            if p!=j:
                x[j].prList.append(p)
                ct+=1
        p+=1

"""               
for i in x:
    print i.prList    


x = []
x.append(student(0))
x.append(student(1))
x.append(student(2))
x.append(student(3))
x.append(student(4))

x[1].prList = [2,3,4]
#x[1].weight = [0,3,2,1]
x[2].prList = [3,1,4]
#x[2].weight = [3,0,1,2]
x[3].prList = [2,4,1]
#x[3].weight = [1,3,0,2]
x[4].prList = [3,2,1]
#x[4].weight = [3,2,1,0]
"""

pwlist = []
newpwlist = []

for i in range(1,len(x)):
    x[i].make(x,i)
    for j in range(0,len(x[i].pairweight)):    
	pwlist.append(x[i].pairweight[j])        
            
pwlist.sort()

for i in range(0,len(pwlist)):
    m = pwlist[i][1][0]
    n = pwlist[i][1][1]
            
    if (not(x[m].ispair or x[n].ispair)):
    	x[m].pair = n
    	x[n].pair = m
    	x[m].ispair = x[n].ispair = True
    	
for i in range(1,len(x)):
    print rmapp[i], "-->", rmapp[x[i].pair]
