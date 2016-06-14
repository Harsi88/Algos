import Gnuplot
import RandomListGenerator
import time
import bruteforce
import better
import efficient
import pdb

lbf = []  # contains time taken by brute-force(order n^3) algorithm
lb = []   # contains time taken by better(order n^2) algorithm
le = []   # contains time taken by efficient(order n) algorithm

for n in range(10,1000,5):
    """
    Plots the comparison between the running time of various algorithms
    to find maximum sum contiguous subsequence.
    Red curve corresponds to Order N^3 algorithm (bruteforce.py)
    Green curve corresponds to Order N^2 algorithm (better.py)
    Blue curve corresponds to order N algorithm (efficient.py) 
    """
    a = []
    RandomListGenerator.generate(n,n,a)    
    
    if n<250:    
        tbf = time.time()
        abf = bruteforce.algo(a)
        ttbf = time.time()
    
        lbf.append((ttbf-tbf)*1000)

    if n<1000:
        tb = time.time()
        ab = better.algo(a)
        ttb = time.time()
    
        lb.append((ttb-tb)*1000)

    te = time.time()
    ae = efficient.algo(a)
    tte = time.time()

    le.append((tte-te)*1000)

g = Gnuplot.Gnuplot(persist=True)
g.title("Maximum Sum Contiguous Sub-sequence")
g.xlabel("Number of entries in list ( divided by 5)")
g.ylabel("Time (in milliseconds)")
g.plot(lbf,lb,le)
