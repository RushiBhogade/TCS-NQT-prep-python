arr=[1,3,4,53,34,6,8,43,5]
k=3
rotatedArry=[]
for i in range(k,len(arr)):
    rotatedArry.append(arr[i])
for i in range(0,k):
    rotatedArry.append(arr[i])    
print(rotatedArry)



### shorterpath

rotatedArry = arr[k::-1]+arr[-1::k]
print(rotatedArry)