#check number string is plaindrome or not
def is_plindrome(s):
    left=0
    right=len(s)-1
    while left < right:
        if(s[left] != s[right]):
           print("not a plaindrome")
        else:
            left+=1
            right-=1
    print("plaindrome")
is_plindrome("madam")           


# remove duplicate by two pointers from array
arr=[1,2,3,4,4,3,2,4,6,7]

i=0                         
while i<len(arr):
    j=i+1
    while j<len(arr):
        if(arr[i]==arr[j]):
           arr.pop(j)
        else:
            j+=1
    i+=1          
print(arr)       




#swap array by two pointers
arr=[1,2,3,4,5]


i=0
j= len(arr)-1

while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
print(arr)    



