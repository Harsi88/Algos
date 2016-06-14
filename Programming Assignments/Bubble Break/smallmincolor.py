import random
import numpy
import sys
import time
import Gnuplot

sys.setrecursionlimit(100000)

l = []

#--- Bursting Clusters

def burst(matrix,i,j,c):
    if i<0 or i>=len(matrix):
        return
    if j<0 or j>=len(matrix[0]):
        return
    if matrix[i][j]==0 or matrix[i][j]!=c:
        return
    matrix[i][j]=0
    burst(matrix,i-1,j,c)
    burst(matrix,i+1,j,c)
    burst(matrix,i,j-1,c)
    burst(matrix,i,j+1,c)
    return

#---

#--- Calculating total Number of colors

def num_color(matrix):
    n = 0
    for i in range(len(matrix)):
        temp = max(matrix[i])
        n = max(temp,n)
    return n

#---

#--- Finding Clusters in the matrix

def cluster(matrix,i,j,c,count):
    if i<0 or i>=len(matrix):
        return count
    if j<0 or j>=len(matrix[0]):
        return count
    if matrix[i][j]==0 or matrix[i][j]!=c:
        return count
    matrix[i][j]=0
    count+=1
    count = cluster(matrix,i-1,j,c,count)
    count = cluster(matrix,i+1,j,c,count)
    count = cluster(matrix,i,j-1,c,count)
    count = cluster(matrix,i,j+1,c,count)
    return count
    

#---

#--- shifting lines to make matrix valid
    
def shift(matrix):
    last_valid = 0
    for j in range(len(matrix[0])):
        i=0
        while i < len(matrix)-1:
            last_valid = -1
            if(matrix[i][j]!=0 and matrix[i+1][j]==0):
                last_valid = i
            counter = i+1
            count = 0
            while(last_valid!=-1 and counter<len(matrix) and matrix[counter][j]==0):
                count+=1
                counter+=1
            for k in range(last_valid,-1,-1):
               
                if matrix[k][j]==0:
                   break
                matrix[k+count][j] = matrix[k][j]
                matrix[k][j] = 0
#                print numpy.matrix(matrix), last_valid, k, i
            if(last_valid!=-1 and count!=0):
                i+=count
            else:
                i+=1
            
#---
    last_valid = -1
    i = len(matrix)-1
    j=0
    while j < (len(matrix[0])-1):
        last_valid = -1
        if matrix[i][j+1]==0:
            last_valid = j
            counter = j+1
            count = 0
        while(last_valid!=-1 and counter<len(matrix[0]) and matrix[i][counter]==0):
            count+=1
            counter+=1
        for k in range(last_valid,-1,-1):
            if matrix[i][k] ==0:
                break
            for l in range(len(matrix)):
                matrix[l][k+count] = matrix[l][k]
                matrix[l][k] = 0
#            print numpy.matrix(matrix), count, last_valid, k, i
            
        if(last_valid!=-1 and count!=0):
            j+=count
        else:
            j+=1
#        print j-1
                
L=[]   
L1 = []
 
def solve(board):
    del L[:]
    del L1[:]
    matrix = board.tolist()
    backup = []
    for i in range(len(matrix)):
        backup.append(list(matrix[i]))
    solve_random(matrix)
    solve1(backup)
    return L,L1
    
def solve_random(matrix):   #--- Deleting the random cluster
    c = num_color(matrix)
#    matrix = board
    #--- Getting Color Count
    color_count = [0]*(c+1)
    backup = []
    for i in range(len(matrix)):
        backup.append(list(matrix[i]))
        for j in range(1,c+1):
            color_count[j]+=matrix[i].count(j)
            
    #---
    #--- Find Clusters
    cluster_loc = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(backup[i][j]!=0):
                count = cluster(backup,i,j,backup[i][j],0)
                if(count > 1):
                    temp = [i,j,count,matrix[i][j]]
                    cluster_loc.append(temp)

    if cluster_loc==[]:
        score = 0
        for i in range(len(L)):
            score+=L[i][1]
        L.append(score)
        return L    
    cluster_loc.sort()
    
    i=random.randrange(len(cluster_loc))
    burst(matrix,cluster_loc[i][0],cluster_loc[i][1],cluster_loc[i][3])
    shift(matrix)    
    L.append([numpy.matrix(matrix),cluster_loc[i][2]**2])
    #---
    solve_random(matrix)
    return L
    
def solve1(matrix):     #--- Deleting the top cluster corresponding to minimum color
    c = num_color(matrix)
#    matrix = board
    #--- Getting Color Count
    color_count = [0]*(c+1)
    backup = []
    for i in range(len(matrix)):
        backup.append(list(matrix[i]))
        for j in range(1,c+1):
            color_count[j]+=matrix[i].count(j)
            
    #---
    #--- Find Clusters
    cluster_loc = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(backup[i][j]!=0):
                count = cluster(backup,i,j,backup[i][j],0)
                if(count > 1):
                    temp = [color_count[matrix[i][j]], count, j, i, matrix[i][j]]
                    cluster_loc.append(temp)

    if cluster_loc==[]:
        score = 0
        for i in range(len(L1)):
            score+=L1[i][1]
        L1.append(score)
        return L1    
    cluster_loc.sort()
    
    j=0
#    count = cluster_loc[0][0]
#    while cluster_loc[j][0]==count:     # for minimum color largest block
#        j+=1
#        if j >= len(cluster_loc):
#            j-=1
#            break
    
    burst(matrix,cluster_loc[j][3],cluster_loc[j][2],cluster_loc[j][4])
    shift(matrix)    
    L1.append([numpy.matrix(matrix),cluster_loc[0][1]**2])
    #---
    solve1(matrix)
    return L1

avg_rand_score,avg_1_score = 0,0
avg_rand_iterations,avg_1_iterations = 0,0
size = 25
iteration = 100
colors = 4

for i in range(iteration):
    sample = [0]*size
    for i in range(size):
        temp = []
        for j in range(size):
#            temp.append(random.randrange(1,colors+1))
            tmp = random.randrange(1,colors+4)
            if(tmp<3):
                temp.append(0)
            elif tmp<6:
                temp.append(1)
            else:
                temp.append(tmp-4)    
        sample[i] = temp

    t = time.time()

    s,l = solve(numpy.matrix(sample))
    t = time.time() - t
    avg_rand_score += s[-1]
    avg_1_score += l[-1]
    avg_rand_iterations+=len(s)
    avg_1_iterations+=len(l)
    print s[-1],len(s),l[-1],len(l),t

print "avg",avg_rand_score/iteration,avg_rand_iterations/iteration,avg_1_score/iteration,avg_1_iterations/iteration
