arr=[1,3,3,4,4,3]

def findEqIndex(arr):
    acTotal=sum(arr)
    left=0
    for i in range(len(arr)):
        right = acTotal - left - arr[i]

        if left == right:
            print("found at",i)
        
        left=left+arr[i]
print(findEqIndex(arr))                