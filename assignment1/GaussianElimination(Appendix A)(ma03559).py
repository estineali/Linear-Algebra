import random, time
from scipy.linalg import lu
#implement a basic GE algorithm and compare it's runtime with that of a library implementation
#elementary row operations

def row_mul(s, lst):
	return [i*s for i in lst]

def row_subt(r2, r1):
	#r2 - r1
	#r1 and r2 are a row of the matrix (in a list)
	assert len(r1) == len(r2)
	return [r2[i] - r1[i] for i in range(len(r1))]

def GE(mat):
	for i in range(1, len(mat)):
		for j in range(i):
			if mat[j][j] == 0:
				return False
			mat[i] = row_subt(mat[i], row_mul(mat[i][j]/mat[j][j], mat[j])) #A(i,j) = 0
	return mat



def generateMatrix(dim):
	return [[random.randint(1, 10) for i in range(dim)] for j in range(dim)]


def main():

	record = open("SelfImplementedGE.csv", "w")
	scipyRecord = open("SciPyGE.csv", "w")

	for i in range(5, 1000, 10):
			
		A = generateMatrix(i) #Matrix for Self Implemented GE
		B = [i.copy() for i in A]

		start_time = time.time()
		
		while GE(A) == False: #if A is singular
			A = generateMatrix(i) #Regenerate a matrix 
			B = [i.copy() for i in A] 
			start_time = time.time() #restart timer

		stop_time = time.time() - start_time
		
		record.write(str(i) + ", " + str(stop_time) + "\n")
		
		start_time = time.time()
		
		pl, u = lu(B, permute_l=True)
		
		stop_time = time.time() - start_time
		
		scipyRecord.write(str(i) + ", " + str(stop_time) + "\n")
		
		
	record.close()
	scipyRecord.close()

main()