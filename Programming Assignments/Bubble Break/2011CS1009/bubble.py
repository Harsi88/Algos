#this is in the bubble-blast repository
import numpy
import os
import random
import pdb
import time
import copy




def colors(N):
	'''colors(M) : Where m is a matrix
	A function that takes a matrix M as input and then gives you
	the total number of colors as output. It converts the set's entries into integers'''
	M=N.copy()
	M=numpy.array(M,int) #converting the matrix entries to integer
	s=set(numpy.reshape(M,M.size)) #consider the set of all elements in the matrix
	s=list(s)#convert the set onto a list, s
	l=len(s) #length of the list is l
	return [s,l]	#returns the list of unique elements, s as well as the length of the list
	#checked!
	


def four_neighbors(N,i,j):
	'''four_neighbors(M,i,j)
	Returns the four neighbors of the i,j the entry of the given matrix M 
	This function returns an array comprising of valid 4-neighbors in the form [(i,j+1), (i+1,j),(i,j-1),(i-1,j)]'''
	M=N.copy()
	r=M.shape[0]#r: number of rows in the matrix M.
	c=M.shape[1]#c: number of columns in the matrix M.

	neighbors=[] #initialise a list by name 'neighbors'
	if (j+1<=c-1): 
		neighbors.append((i,j+1)) #append the RIGHT neighbor
	if (i+1<=r-1):
		neighbors.append((i+1,j)) #append the BELOW neighbor
	if (j-1>=0):
		neighbors.append((i,j-1)) #append the LEFT neighbor
	if (i-1>=0):
		neighbors.append((i-1,j)) #append the ABOVE neighbor
	return neighbors #return the list of 4-neighbors


	


#Create a function that takes matrix as input and blasts the i,j th
#position, if it can be blasted i.e. 

def block(N1,i,j):
	'''returns a block of elements surrounding the i,j th block that is supposed to be blasted,
	as per the rules of the bubble blast game
	format: block(M,i,j)'''
	M=N1.copy()
	seen=set([]) # A set of elements seen so far
	block_list=[(i,j)] # The required block comprising of same colored balls
	s=set([(i,j)]) #initialise the set s with (i,j) which is passed as a parameter to the function
	b=[(i,j)]
	while len(s) != 0: #repeat until the set becomes empty
		set_element=s.pop() #pop an element from the set
		seen.add(set_element) #include this element to the list 'seen' which denotes that
				      #this element was visited.
		p=set_element[0] #the element popped will be of the form (p,q)
		q=set_element[1]
		nei=four_neighbors(M,p,q) #consider the 4 neighbors of p,q
		for N in nei: #iterate through all neighbors of p,q
			if M[p,q] == M[N] and N not in seen: 
			#if the entries of p,q is equal to one of its neighbors
			#and if (p,q) has not been visited so far, then do the following:
				s.add(N)#add these neighbors to s
				block_list.append(N) #include the new element to the block
			seen.add(N)
	return block_list
	#checked!

def checkzerorow(N,i):
	'''Check if the ith row of M is a  zero row. First row in the matrix is referred to as zeroth row'''
	M=N.copy()
	r=M.shape[0]
	c=M.shape[1]
	flag=1
	for k in range(c): 
		if M[i,k] != 0:
			flag =0
	return flag
	#checked!!

def checkzerocolumn(N,i):
	'''Check if the ith column of M is a  zero row. First row in the matrix is referred to as zeroth row'''
	M=N.copy()
	r=M.shape[0]
	c=M.shape[1]
	flag=1
	for k in range(r): 
		if M[k,i] != 0:
			flag =0
	return flag
	#checked!
	


def swaprows(N,i,j):
	'''Input (Matrix M, row number i, row number j) and returns a matrix with i and jth rows swapped'''
	M=N.copy()
	l=M[i,:].copy()	#copy elements of the ith row onto a list 'l'.
	M[i,:]=M[j,:].copy() #copy elements of jth row onto ith row
	M[j,:]=l.copy() #copy elements in the list 'l' onto jth row
	return M
	#checked

def swapcolumns(N,i,j):
	'''Input (Matrix M, column number i, column number j) and returns a matrix with i and jth columns swapped'''
	M=N.copy()	
	l=M[:,i].copy()	#copy elements of the ith column onto a list 'l'.
	M[:,i]=M[:,j].copy() #copy elements of jth column onto ith column
	M[:,j]=l.copy() #copy elements in the list 'l' onto jth column
	return M
	#checked!


def springcolumn(N,c): #bring up row r to the top, like in the bubble blasting game with a zero row!
	'''Input is a matrix M and the column number c, the function returns a matrix with column c sprung up to first column and
	pushing all the other columns one step to the left'''
	M=N.copy()
	for j in range(c,0,-1): #for loop from 'c' down to 1
		M=swapcolumns(M,j,j-1)
	return M


def pushup_zero(N,r,c):
	'''push the r,c th entry to the top and shift all the elements above, one step down'''
	M=N.copy() #pass by parameter
	for i in range(r,0,-1): #countdown i  from r to 0 (This is to swap the entries)
		M[i,c],M[i-1,c]=M[i-1,c],M[i,c]	 #swap the ith row and the i-th row (cth-column remains constant)
	return M
	#checked!



def clean_zero(N): 
	'''This function takes a matrix and finds a zero and pushes it up just the way it happens in the bubble blast game'''
	M=N.copy() #pass by parameter.
	r=M.shape[0] #r: number of rows in the matrix.
	c=M.shape[1] #c: number of columns in the matrix.
	for i in range(c): #iterate through the columns.
		flag=0 #with a flag which tells you whether there has been a non-zero element seen so far. 
		for j in range(r): #iterate through the rows.
			if M[j,i]!=0: #if the entry isn't 0.
				flag=1 #flag =1 stating that a non-zero entry is just seen.
			if M[j,i]==0 and flag==1: #in case we see a zero after seeing a non-zero.
				M=pushup_zero(M,j,i) #push this zero up as in the bubble blast game. 
	return M
				

					
def purify_matrix(N):
	'''purify_matrix(M) removes zero rows and zero columns by shifting the matrix entries in accordance with the 
	bubble blast game.'''
	M=N.copy()
	r=M.shape[0] #r: number of rows in the matrix M
	c=M.shape[1] #c: number of columns in the matrix M
	
	#the following code checks for the presence of a zero row and then removes it by shifting the above rows one step down.

	M=clean_zero(M) #clear all blasted bubbles. 
	#the following code checks for the presence of a zero column and then removes it by shifting the column on the left
	#one step to the right. 
	for j in range(c): #for all the columns in the matrix
		if checkzerocolumn(M,j)==1: #check if there is a zero column
			M=springcolumn(M,j)     #when you find a zero column, spring that column to the top (first column)

	return M
	#checked!
		
			

def blast(N,i,j):
	M=N.copy() #This is equivalent to pass by parameter
	'''blast(M,i,j): returns the matrix with i,jth block blasted
	Blasts the i,jth entry that is being passed according to the rules of
	the bubble blast game. Returns the resulting matrix'''
	if M[i,j]!=0: #there is nothing to blast if the i,j th entry is 0.	
		block_list=block(M,i,j) #block the bunch of entries that have the same color
					#After blocking, blast them, this is equivalent to assigning 0 to all the 
					#entries.
		if len(block_list)>1: #ensure that the block has more than 1 bubble
			for i in block_list: #blasts the block by filling zeros in it. Note that the i here is a 2 tuple.
				M[i]=0	#i is a 2 tuple (_,_) which stands for an entry in the matrix
		#else:
			#print "There is nothing to blast, your block comprises of single bubble" #error message (exception handling)

		#The code below takes care of empty row and column
		M=purify_matrix(M)

	return M

def valid_couple(M,N):
	'''Checks if the input matrix M gives N when a block is bursted
	returns flag
	flag=0 if its invalid 1 if its valid'''

	A=M.copy() #pass by parameter equivalent
	B=N.copy() #pass by parameter equivalent
	flag=0 #declare that the matrices are not couples in the chain
	if (numpy.shape(A)==numpy.shape(B)): #ensure that the two matrices are of the same dimension
		r=A.shape[0] #r stands for the number of rows
		c=A.shape[1] #c stands for the number of columns
		S=set([]) #initialize a set data structure
		for i in range(r):
			for j in range(c):
				S.add((i,j)) #populate S with all possible (i,j) pairs
		while len(S)>0: #ensure that the set is non-empty
			x=S.pop() #pop an element from the set
			b=block(A,x[0],x[1]) #find the block of elements in the given 
					     #matrix at the x[0] and x[1]th entry
			b.remove(x) #remove the popped out element from b
			for k in b: #iterate through the elements of the block
				if (len(S)>0): #ensuring that S is non-empty...
					S.remove(k) #remove all elements in the block from the set S
			Q=blast(A,x[0],x[1]) #Q is a new matrix, obtained after A is blasted at
					     #x[0],x[1]
			if (numpy.array_equal(Q,B)) and (not (numpy.array_equal(A,Q))):
				#if the resultant matrix Q is different from A and is actually a valid next matrix, then assign flag=1
				flag=1


	else:
		print "Error! the matrices are of different sizes"
	return flag

def compute_score(A,B):
	'''Computer the score in the bubble blast game, if we were to obtain the matrix B from
	the matrix A by bubble blasting a block. We assume here that the sequence A to B is valid,
	and compute the score'''
	M=A.copy() #pass by parameter
	N=B.copy() #pass by parameter
	countzeroM=0 #initialise the variable to 0, this will contain the number of zeroes in M
	countzeroN=0 #initialise the variable to 0, this will contain the number of zeroes in N

	listM=M.tolist() #convert the matrix onto a list, this will be lists of lists
	listN=N.tolist() #convert the matrix onto a list, this will be lists of lists
	for i in range(len(listM)):
		countzeroM=countzeroM+(listM[i].count(0))

	for i in range(len(listN)):
		countzeroN=countzeroN+(listN[i].count(0))

	score= (countzeroN-countzeroM)
	score= score*(score)
	return score

def valid_chain(M0,D,echo):
	'''The input to this function is a chain of matrices [[(M1,s1),(M2,s2),(M3,s3)...(Mk,sk)],s],
	csl356 students were asked to return the solution in this format. The current function checks for the validity of this output. M0
	here stands for the input matrix.
	if echo is assigned 1 (3rd parameter in the function), the program displays interactive messages'''
	C=copy.deepcopy(D) #pass by parameter

	C[0].insert(0,(M0,0)) #include the input matrix as the first matrix M0, with s0 being 0.
	valid=1
	L=C[0] #L contains the list [(M1,s1),(M2,s2),(M3,s3)...(Mk,sk)]
	s=C[1] #s stands for the total score. 		

	M_chain=[] #this will contain the chain of matrices [M1,...Mk]
	score_chain=[] #this will contain the sequence of scores [s1,...sk]
	for i in range(len(L)):
		M_chain.append(L[i][0]) #flood M_chain
		score_chain.append(L[i][1]) #flood score_chain

	if echo==1:
		os.system("clear")
		print "You have entered a matrix of dimension:", M0.shape
		print "There are ",len(M_chain)," number of matrices in your answer"
		time.sleep(2)

	for i in range(len(M_chain)-1):
		if echo==1:#echoes
			print "Verifying Matrix number ",i," of ",len(M_chain),"(in process)" #echos if 'echo' variable is passed as 1
			#doesn't echo otherwise
		if valid_couple(M_chain[i],M_chain[i+1])==0: #checks if the the i and i+1 the matrix are valid transformations
			valid=0
			print "The matrices ",i,"-->",i+1," in the sequence are invalid"
			return valid,i,i+1 #return (0,i,i+1) : which means the i and i+1th matrices are invalid.

		if ( (compute_score(M_chain[i],M_chain[i+1])) != score_chain[i+1]) : #checks if the score is computed properly 
								    		     #from the ith to i+1th transformation.
			valid=0 #term it invalid
			print "The matrices ",i,"-->",i+1," in the sequence are reported with an incorrect score"
			return valid,i,i+1 #return (0,i,i+1): denoting that i and i+1th matrix score is invalid

	#the if loop below checks for the correctness of the sum of scores.
	if s!=numpy.sum(score_chain): #check if the sum 's' is correct or incorrect.
		print "Sum of the scores is incorrect!"
		valid=0 #report invalid (return)

	return valid,-1,-1 #returns (1,-1,-1) if the sequence is valid, or (0,-1,-1) if it is invalid.

def ranmat(m,n,k):
	'''Create a random matrix of the order m X n with entries {1,2,3,...,k}'''
	M=numpy.zeros((m,n)) #construct a zero matrix of dimension m X n
	for i in range(m): 
		for j in range(n):
			M[i,j]=random.randint(1,k) #flood the matrix with random entries with values {1,2,...,k}
	return M



