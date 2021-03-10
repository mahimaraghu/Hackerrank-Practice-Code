def print_formatted(number):
    
    for i in range (1,number+1):
        decimal=str(i)
        octal=oct(i).lstrip("0o")
        hexadecimal=hex(i).lstrip("0x").upper()
        binary=bin(i).lstrip("0b")
        print(decimal.rjust(len(bin(number).lstrip("0b"))," ")+ ' '+octal.rjust(len(bin(number).lstrip("0b"))," ")+' '+hexadecimal.rjust(len(bin(number).lstrip("0b"))," ")+' '+binary.rjust(len(bin(number).lstrip("0b"))," "))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)