from array import array
 
n=int(input('Enter the lenth of array'))
target=int(input('Enter the target'))
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

# Solution 2 with time complexity O(n)
def Results(arr,target):
    result=[]
    index_value={}
    for i,arr in enumerate(arr):
        difference= target-arr
        if difference in index_value:
            result.append(index_value[difference])
            result.append(i)
            break
        else:
            index_value[arr]=i
    return result
a= Results(arr,target)
print(a)