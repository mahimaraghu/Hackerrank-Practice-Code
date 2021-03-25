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

