import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
print(a)
swaps=0
if (a==sorted(a)):
    print("swaps",swaps)
    print("first",a[0])
    print("last",a[-1])
    sys.exit(0)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
            swaps+=1
print("swaps",swaps)
print("first",a[0])
print("last",a[-1])
        
            
    
    





##for (int i = 0; i < n; i++) {
##    // Track number of elements swapped during a single array traversal
##    int numberOfSwaps = 0;
##    
##    for (int j = 0; j < n - 1; j++) {
##        // Swap adjacent elements if they are in decreasing order
##        if (a[j] > a[j + 1]) {
##            swap(a[j], a[j + 1]);
##            numberOfSwaps++;
##        }
##    }
##    
##    // If no elements were swapped during a traversal, array is sorted
##    if (numberOfSwaps == 0) {
##        break;
##    }
##}
