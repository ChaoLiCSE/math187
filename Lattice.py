import functools
import operator

#this is a dot product on two vectors
def dot(vector1, vector2):
    dotProduct = functools.reduce( operator.add, map( operator.mul, vector1, vector2))
    return dotProduct

def orthognal(vector1, vector2):
	if(dot(vector1, vector2) == 0):
		return True
	return False

def norm(vector):
    out = "the norm of the vector is: "+ str(dot(vector, vector)) + "^(1/2)"
    print(out)
    return (dot(vector, vector) **(1/2))

def matrix(w,h):
    Matrix = [[0 for x in range(h)] for y in range(w)] 
    return Matrix

def printMatrix(matrix):
    print("")
    for i in range(len(matrix)):
        #out ="["
        out = ""
        for j in range(len(matrix[1])):
    	    out += (str(matrix[i][j])+" ")
        #out+="]"
        print(out)
    print("")

def matrixMult(A,B):
	#first find the width and lenth of A, B
    Awidth = len(A) 
    Alength = len(A[0])

    Bwidth = len(B)
    Blength = len(B[0])

    #then the result matrix should be Awidth * Blength
    result = matrix(Awidth, Blength)
    printMatrix(result)
    for i in range(len(A)):
	   # iterate through columns of Y
       for j in range(len(B[0])):
           # iterate through rows of Y
           for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def vectorMin(vector1, vector2):
	ret = [0]*len(vector1)
	for i in range(len(vector1)):
		ret[i] = vector1[i]-vector2[i]

	return ret

def multVectorWithNum(num, vector):
	ret = [0]*len(vector)
	for i in range(len(vector)):
		ret[i] = num*vector[i]

	return ret

'''
A = [31,59]
B= [37, 70]
print(LatticeReduction(A, B))

'''
def LatticeReduction(vector1, vector2):
    print(vector1)
    print(vector2)
    norm1 = norm(vector1)
    norm2 = norm(vector2)

    print("norm1 = "+ str(norm1) +", and norm2 = "+str(norm2))

    if(norm1 > norm2):
    	print("Therefore, swap")
    	temp = vector1
    	vector1 = vector2
    	vector2 = temp

    else:
    	print("not swap")

    t = round(dot(vector1, vector2)/dot(vector1, vector1))
    print("t = "+str(t))

    if(t == 0):
    	print("the base is: " + str(vector1) + " and "+ str(vector2))
    	return (vector1,vector2)
    
    newV2 = vectorMin(vector2 ,multVectorWithNum(t, vector1))
    print(vector1)
    print(newV2)
    return LatticeReduction(vector1, newV2)

def toMatrix(vector):
    ret = matrix(len(vector), len(vector))
    count = 0
    for i in range(len(vector)):
        for j in range(len(vector)):
            ret[j][i] = vector[(j - count) % len(vector)]
        count+=1

    print("the rearranged value is: ")
    printMatrix(ret)
    return ret

def matrixVectorMult(A, B):
    Awidth = len(A) 
    Alength = len(A[0])

    Bwidth = len(B)

    #then the result matrix should be Awidth * Blength
    result = [0]*len(B)

    for i in range(len(A)):
	   # iterate through columns of Y
           # iterate through rows of Y
           for k in range(len(B)):
                result[i] += A[i][k] * B[k]

    return result

def star(coeff1, coeff2):
    
    return matrixVectorMult( toMatrix(coeff1), coeff2)
	
print(star([-1,4,1],[3,-1,5]))

def modVector(prime, vector):
	for i in range (len(vector)):
		vector[i] = vector[i] % prime
	return vector

#this is a function that brutally find the inverse of a given number
#and integer
def findinv(num, prime):
    for i  in range(0, prime):
        if(i * num % prime == 1):
        	return i

    return -1

print(LatticeReduction([90,123],[56,76]))