import fractions
from fractions import Fraction

#this is a function used to find a, if the slope 
#does not exist it will return 'inf'
def findSlope(point1, point2, A):
	
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    #case P=Q
    if(point1 == point2):
        #the vertical tangent line
        if(y2 == 0):
            return "inf"

        upp = (3* x1**2 + A)
        down = (2*y1)
        gcd = fractions.gcd(upp, down)
        upp = upp/gcd
        down = down/gcd

        print("the slope is: ")
        print ("%d / %d" % (upp,down))
        return [upp,down]

    #vertical line
    if(x1 == x2):
	    return "inf"

    upp = (y2-y1)
    down = (x2-x1)
    gcd = fractions.gcd(upp, down)
    upp = upp/gcd
    down = down/gcd

    print("the slope is: ")
    print ("%d/%d" % (upp,down))
    return [upp,down]


#usage: A is the A stated in x^3 + Ax + B = y^2
#retVal: the simple P+Q output
def findPoint4(point1, point2, A):
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    a = findSlope(point1, point2, A)
    
    #the zero point case
    if(a == "inf"):
    	print ("slope does not exist, no x3")
    	return ["inf", "inf"]
    
    upp = a[0]
    down = a[1]

    #calculate normal P3
    x3 = Fraction((upp/down) **2 - x2 - x1).limit_denominator()
    y3 = Fraction(y1 + (upp/down)*(x3 - x1)).limit_denominator()

    P4 = [x3, -y3]

    out = "the P4 is: (" + str(P4[0]) + "," + str(P4[1]) + ")"
    print(out)

    return P4

#this is a function used to find a, if the slope 
#does not exist it will return 'inf'
def findSlopewithprime(point1, point2, A, prime):
	
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    #case P=Q
    if(point1 == point2):
        #the vertical tangent line
        if(y2 == 0):
            return "inf"
        
        upp = (3* x1**2 + A) % prime
        down = findinv((2*y1), prime)

        a = upp * down % prime
        return a

    #vertical line
    if(x1 == x2):
	    return "inf"

    upp = (y2-y1) % prime
    down = (x2-x1) % prime
    a = upp * down % prime

    print("the slope is: ")
    print(a)
    return a


#usage: A is the A stated in x^3 + Ax + B = y^2
#retVal: the simple P+Q output
def findPoint4withPrime(point1, point2, A, prime):
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    a = findSlopewithprime(point1, point2, A, prime)
    
    #the zero point case
    if(a == "inf"):
    	print ("slope does not exist, no x3")
    	return ["inf", "inf"]

    #calculate normal P3
    x3 = (a **2 - x2 - x1) % prime
    y3 = (y1 + a*(x3 - x1)) % prime

    P4 = [x3, -y3]

    out = "the P4 is: (" + str(P4[0]) + "," + str(P4[1]) + ")"
    print(out)

    return P4

#this is a function that brutally find the inverse of a given number
#and integer
def findinv(num, prime):
    for i  in range(0, prime):
        if(i * num % prime == 1):
        	return i

    return -1

#get the result such as 3P, 5P
#ex: result should be [13, 2]
#print (multwithprime(5, [1,8], 3, 13))
#this function only works for with prime situation
def multwithprime(time, point, A, prime):
    print("start to mult: ")
    print(time)

    if(time < 2):
        return point

    if(time == 2):
        result = findPoint4withPrime(point, point,A, prime)

        #print (result[0].numerator % prime)
        #print("inv: ")
        #print(result[0].denominator)
        x = (findinv(result[0].denominator, prime) * (result[0].numerator % prime) % prime)
        y = (findinv(result[1].denominator, prime) * (result[1].numerator % prime) % prime)

        return [x,y]

    result = findPoint4(point, multwithprime( time-1, point, A, prime), A)
    x = (findinv(result[0].denominator, prime) * (result[0].numerator % prime) % prime)
    y = (findinv(result[1].denominator, prime) * (result[1].numerator % prime) % prime)

    out = "the outcome of " + str(time) +" * "+ str(point) +  " is: " +  str(x) + " , "+str(y)  
    print(out) 
    return [x,y]

#print(findPoint4([1,2], [7,16],-15))
#print(findPoint4([0,0],[0,0],1))
