arr=[1,2,3,2,3,4]

left=[0]*len(arr)
right=[0]*len(arr)
    #find right max
left[0]=arr[0]
for i in range(1,len(arr)):
    left[i]=max(left[i-1],arr[i])

#find left side max
right[len(arr)-1] = arr[len(arr)-1]
for j in range(len(arr)-2,-1,-1):
    right[j]=max(right[j+1],arr[j])

water =0
print(left,right)
for i in range(len(arr)):
    water+=min(left[i],right[i]) - arr[i]
print(water)    
