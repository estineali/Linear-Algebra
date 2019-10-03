import numpy as np
import scipy
import scipy.linalg
import time
import matplotlib.pyplot as plt
def create_square_matrix(_type,order):
    if _type == 1:
        return scipy.random.randint(1,200,(order,order))
    if _type == 2:
        return numpy.random.randint(1,200,(order,order))
    
timeListLU=[]
sizeListLU=[]
timeListG=[]
def makeGraph(n):
    
    for i in range(8,n,1):
        A = create_square_matrix(1,i)
        a=time.clock()
        LU = scipy.linalg.lu_factor(A)
        for j in range (i):
            b=scipy.random.randint(1,20,(i,1))
            result=scipy.linalg.lu_solve(LU,b)   
        b=time.clock()
        
        sizeListLU.append(i)
        print(i)
        timeListLU.append(b-a)
        a=time.clock()
        for j in range (i//8):
            b=scipy.random.randint(1,20,(i,1))
            result=np.linalg.solve(A,b)
        b=time.clock()
        timeListG.append(b-a)
    plt.plot(sizeListLU,timeListG)
    plt.plot(sizeListLU,timeListLU)
    
    ## plt.plot(sizeListLU,[(a*i)**3 for i in sizeListLU])
    plt.show()


makeGraph(200)

##    print ("P:")
##    pprint.pprint(P)
##
##    print ("L:")
##    pprint.pprint(L)
##
##    print ("U:")
##    pprint.pprint(U)
