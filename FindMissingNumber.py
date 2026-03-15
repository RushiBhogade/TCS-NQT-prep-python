arr=[1,2,3,4,6,7,8,9]
n=9
missngNumber=0

def sumofarr(arr):
    sum=0
    for num in arr:
        sum+=num
    return sum

def findMissingNumber(arr,n):
    total= n*(n+1)//2 # formula to find tottal 
    simofarr = sumofarr(arr)  # here use sum keyword or use loop
    missngNumber=total - simofarr
print(missngNumber)

findMissingNumber(arr,n)
