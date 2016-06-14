import random
import numpy
import sys
import time

sys.setrecursionlimit(10000000)     #--- to increase recursion depth for larger matrix sizes
l = []

#--- Method to Burst Clusters

def burst(matrix,i,j,c):
    """ This function bursts the clusters represented by indices i and j."""
    if i<0 or i>=len(matrix):  # Terminating conditions.
        return
    if j<0 or j>=len(matrix[0]): # Terminating conditions.
        return
    if matrix[i][j]==0 or matrix[i][j]!=c: # terminating conditions.
        return
    matrix[i][j]=0
    burst(matrix,i-1,j,c)            # Recursive calls on four neighbours.
    burst(matrix,i+1,j,c)
    burst(matrix,i,j-1,c)
    burst(matrix,i,j+1,c)
    return

#---

#--- Calculating total Number of colors

def num_color(matrix):
    """ Calculate the number of colors in the input matrix."""
    n = 0
    for i in range(len(matrix)):
        temp = max(matrix[i])
        n = max(temp,n)
    return int(n)

#---

#--- Finding Clusters in the matrix

def cluster(matrix,i,j,c,count):
    """ Check whether at given indices i and j, there exist a cluster or not."""
    if i<0 or i>=len(matrix):
        return count
    if j<0 or j>=len(matrix[0]): # Terminating conditions.
        return count
    if matrix[i][j]==0 or matrix[i][j]!=c:
        return count
    matrix[i][j]=0
    count+=1
    count = cluster(matrix,i-1,j,c,count)  # Recursive calls on neighbours.
    count = cluster(matrix,i+1,j,c,count)
    count = cluster(matrix,i,j-1,c,count)
    count = cluster(matrix,i,j+1,c,count)
    return count
    

#---

#--- shifting lines to make matrix valid
    
def shift(matrix):
    """ Shifting Vertically and Horizontally to make a valid matrix. """
    last_valid = 0
    for j in range(len(matrix[0])):
        i=0
        while i < len(matrix)-1:           # Loop till i becomes greator than matrix length.
            last_valid = -1
            if(matrix[i][j]!=0 and matrix[i+1][j]==0):    # Vertical shift condition check.
                last_valid = i
            counter = i+1
            count = 0
            while(last_valid!=-1 and counter<len(matrix) and matrix[counter][j]==0):  # Checking for number of shifts required.
                count+=1
                counter+=1
            for k in range(last_valid,-1,-1):  # Vertical shifting.
               
                if matrix[k][j]==0:
                   break
                matrix[k+count][j] = matrix[k][j]
                matrix[k][j] = 0
            if(last_valid!=-1 and count!=0):  # Incrementing i to valid position.
                i+=count
            else:
                i+=1
            
    #--- Shifting horizontally
    last_valid = -1
    i = len(matrix)-1
    j=0
    while j < (len(matrix[0])-1):                  # Loop till i becomes greator than matrix length.
        last_valid = -1
        if matrix[i][j+1]==0:       # Horizontal shift condition check.
            last_valid = j
            counter = j+1
            count = 0
        while(last_valid!=-1 and counter<len(matrix[0]) and matrix[i][counter]==0):     # Checking for number of shifts required.
            count+=1
            counter+=1
        for k in range(last_valid,-1,-1):       # Horizontal shifting.
            if matrix[i][k] ==0:
                break
            for l in range(len(matrix)):
                matrix[l][k+count] = matrix[l][k]
                matrix[l][k] = 0
            
        if(last_valid!=-1 and count!=0):     # Incrementing i to valid position.
            j+=count
        else:
            j+=1
                
L1 = [] #--- List to store output

#--- Call this method to solve the numpy matrix 
def solve(board): 
    """ Take input as numpy matrix and returns a list of matrices and scores at each step."""
    del L1[:]
    del l[:]
    matrix = board.tolist() #--- Converting numpy matrix to list of list
    solve1(matrix)
    return L1

#--- Main method to solve a given matrix, input is taken in the from of list        

def solve1(matrix):     #--- STRATEGY ADOPTED:Deleting the top cluster corresponding to minimum color
    c = num_color(matrix)

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
                    temp = [color_count[int(matrix[i][j])],i,j,count,matrix[i][j]]
                    cluster_loc.append(temp)

    #--- If no cluster is left than return
    if cluster_loc==[]:
        score = 0
        L1.append(l);
#        print(L1);
        for i in range(len(L1[0])):
            score += L1[0][i][1]
          
        L1.append(score)
        return L1    

    #--- Sort clusters on basis of "color count" than its "location from top" than "size of cluster"
    cluster_loc.sort()
    
    #--- Burst the first cluster from sorted list of clusters
    burst(matrix,cluster_loc[0][1],cluster_loc[0][2],cluster_loc[0][4])
    #--- Make matrix valid by shifting elements
    shift(matrix)
    #--- Appending result in output list    
    temp  = numpy.matrix(matrix),cluster_loc[0][3]**2;
    l.append(temp);
#    L1.append([numpy.matrix(matrix),cluster_loc[0][3]**2])
    #---
    solve1(matrix)
    return L1

