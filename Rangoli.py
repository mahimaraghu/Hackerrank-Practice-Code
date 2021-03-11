def print_rangoli(size):
    n = size
    
    ans = ""
    
    if(n > 26):
        print('enter valid number')
    else:
        lst=[]
        maxAsci = 97+n
        for i in range(97, maxAsci ):
            lst.append(chr(i))

    maxLength = 2 * ( 2*n - 1) - 1

    def printLine(lst):
        lstTemp = list(lst[1:])
        lstTemp.reverse()
        lstTemp.extend(lst)
        wStr = "-".join(lstTemp)
        return wStr.center(maxLength, "-")
    for i in range(1,n):
        l = lst[-i:]#lst[-1:] last element
        ans += "{}\n".format(printLine(l))
    for i in range(n,0 , -1):
        l = lst[-i:]#lst[-n:] 
        ans += "{}\n".format(printLine(l))
        
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)