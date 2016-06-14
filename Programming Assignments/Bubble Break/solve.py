import sys
import random
import numpy

board = numpy.arange(625).reshape(25,25)
inCluster = numpy.arange(625).reshape(25,25)
sizeCluster = numpy.arange(625).reshape(25,25)

def printtt():
    for i in range(0,25):
        for j in range(0,25):
            inCluster[i][j] = sizeCluster[i][j] = 0
    return

def printt():
    for i in range(0,25):
        for j in range(0,25):
            print board[i][j],
        print 
    return

cluster = [[]];

def findCluster():
    for i in range(0,25):
        for j in range(0,25):
            if board[i][j]==board[i+1][j]:
                    inCluster[i][j]=inCluster[i+1][j]=1
                    

for i in range(0,25):
    for j in range(0,25):
        temp = random.randrange(0,5)
        board[i][j] = temp;
        if temp==0:
            board[i][j] = 5;
#        print board[i][j],
#    print 

print board
#printt()
