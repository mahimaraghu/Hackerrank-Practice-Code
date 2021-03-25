def merge_the_tools(string, k):
       
    parts = k 
    arr=[]
    i_res = []
    for i in range(0,len(string),parts):
        
        part= string[i:i+parts]
            
        arr.append(part)  
    for i in arr:
        for j in i:
            if j not in i_res:
                i_res.append(j)
        print("".join(i_res))
        i_res=[]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
