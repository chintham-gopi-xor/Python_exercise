numbers = list(range(0, 200, 2))  

def linear_search(n):
    comp=0
    leng=len(numbers)
    for i in range(leng):
        
        if numbers[i] ==n :
            return i,comp
        comp +=1
    return -1,comp

def binary_search(n,end=None,first=0,comp=0):
    if end is None:
        end = len(numbers) - 1
    if first>end:
        return -1,comp
    mid=(first+end)//2
    if(numbers[mid]==n):
        return mid,comp
    if numbers[mid]<n:
        first=mid+1
    if numbers[mid]>n:
        end=mid-1
    comp +=1
    return binary_search(n,end,first,comp)
    
print("linear 150:", linear_search( 150))
print("binary 150:", binary_search( 150))
print("linear 151:", linear_search( 151))
print("binary 151:", binary_search( 151))
