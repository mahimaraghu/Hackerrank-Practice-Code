##import numpy
##import ast
##N=int(input())
##n=[]
##inp=[]
##for i in range(N):
##    n.append(input().split(" "))
##print(n)
###inp.append([ast.literal_eval(i) for i in n]) 
##for i in n:
##    inp.append(ast.literal_eval(i))
##print(n)
##print(inp)
##arr2=numpy.array(inp) # n or inp? inp me kiya h na append ast krne ke ibaaad yesh ussi ko ra khna
##print(arr2)


import numpy
numpy.set_printoptions(legacy='1.13')
import ast
N=int(input())

inp=[]
for i in range(N):
    n=[float(x) for x in input().split(" ")]
    inp.append(n)

arr=numpy.array(inp)
print(round(numpy.linalg.det(arr),2))

##import numpy
##n=int(input())
##a=numpy.array([input().split() for _ in range(n)],float)
##numpy.set_printoptions(legacy='1.13') #important
##print(numpy.linalg.det(a))

