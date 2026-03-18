#prodct of array prifixx we can solve by brute force 

arr=[1,2,3,2,2,1]


left=[1]*len(arr)
right=[1]*len(arr)


for i in range(1,len(arr)):
    left[i]=left[i-1] * arr[i-1]

for i in range(len(arr)-2,-1,-1):
    right[i]=right[i+1] * arr[i+1]    

Result=[]

for i in range(len(arr)):
    Result.append(left[i] * right[i])
print(Result)    