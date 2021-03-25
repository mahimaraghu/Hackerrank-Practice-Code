import numpy
A=[]
B=[]
N=int(input())
for i in range(N):
    n=[int(x) for x in input().split(" ")]
    A.append(n)
for i in range(N):
    m=[int(x) for x in input().split(" ")]
    B.append(m)
print(A)
print(B)
A_arr=numpy.array(A)
B_arr=numpy.array(B)
print(A_arr)
print(B_arr)
print(numpy.dot(A,B))
