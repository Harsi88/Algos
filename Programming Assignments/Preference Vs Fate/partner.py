import string

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
nmapp = {}
c = 1
for j in range(1,41):
    l = 0
    line = f.next()
    fields = line.split(',')
    for i in fields[1:3]:
        l += 1
        if l==1:
            mapp[i.strip().upper()] = c
            rmapp[c] = i.strip().upper()
        else:
            nmapp[c] = i.strip().upper()
            c+=1

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

pwlist = []

for i in range(1,len(x)):
    x[i].make(x,i)
    for j in range(0,len(x[i].pairweight)):    
	pwlist.append(x[i].pairweight[j])        
            
pwlist.sort()

i=0
while i<len(pwlist):
    m = pwlist[i][1][0]
    n = pwlist[i][1][1]

    topair = True

    for j in range (1,x[m].prList.index(n)):
        if not(x[x[m].prList[j]].ispair):
            topair = False
            break

    for j in range (1,x[n].prList.index(m)):
        if not(x[x[n].prList[j]].ispair):
            topair = False
            break
    i+=1        
                
    if (not(x[m].ispair or x[n].ispair)) and topair:
    	x[m].pair = n
    	x[n].pair = m
    	x[m].ispair = x[n].ispair = True
    	i = 0
        	
for i in range(1,len(x)):
    print string.ljust(nmapp[i],25),",",string.ljust(rmapp[i],11), "   -->   ", string.ljust(nmapp[x[i].pair],25),",",string.ljust(rmapp[x[i].pair],12)
#    print "%12d %12d" % (nmapp[i] , rmapp[i])

