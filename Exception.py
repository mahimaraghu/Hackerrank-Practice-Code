t=int(input())
inArr = []
out=[]
for i in range(t):
    inArr.append(input())

def getOP(inp): # string of 1 line input
    a,b = inp.split(" ")
    try:
        # '0', '#', '1'
        if(type(int(b)) != int):
            raise ValueError

        d= int(a)//int(b)
        return d
    except ValueError as f:
        return "Error Code: {0}".format(f)
    except ZeroDivisionError as e:
        return "Error Code: {0}".format(e)

for j in range(t):
    out.append(getOP(inArr[j]))

for i in out:
    print(i)