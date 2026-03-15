arr=[1,2,3,7,5]
target=3

start=0
curr_sum=0
sumOfarr= sum(arr)
if target>sumOfarr:
    print("No subarray with the given sum exists.")

for end in range(len(arr)):
    
    curr_sum+=arr[end]
    
    while curr_sum>target:
        curr_sum-=arr[start]
        start+=1
        
    if curr_sum==target:
        print("Subarray:",arr[start:end+1])
        break