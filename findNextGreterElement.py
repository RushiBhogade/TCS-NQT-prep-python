# find next grether element in array if not print -1

arr=[1,23,34,3,74,56]

newarr=[]
i=0


while i < len(arr):
    j=i+1
    found=False
    while j < len(arr):
        if arr[i] < arr[j]:
            newarr.append(arr[j])
            found=True
            break
        j+=1
    i+=1            
    if found ==False:
        newarr.append(-1)
print(newarr)                

# by the stack

def bySolveStack(arr):
    stack=[]
    result = len(arr) * [-1]

    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1] < arr[i]:
            stack.pop()
        if stack:
            result[i]=stack[-1]    
        stack.append(arr[i])

    return result
print(bySolveStack([1,2,4,10,1]))




