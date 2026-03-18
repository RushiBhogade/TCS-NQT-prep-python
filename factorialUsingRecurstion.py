def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5)) 



# sun of array
arr=[1,2,3,4,5]
def sumofArray(arr,n):
    if(n==0):
        return arr[0]
    else:
        return arr[n]+sumofArray(arr,n-1)
print(sumofArray(arr,len(arr)-1))


# fibonacci series
def fibonacci(n):
    if(n==0):
        return 0
    else:
        if(n==1):
            return 1
        else:
            return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))


# factroial without division and multiplication


def countsum(sumss,n):
    result=0
    for i in range(n):
        result+=sumss
    return result    
        

def factroiral(n):
    sums=1
    for i in range(1,n+1):
        sums=countsum(sums,i)
    return sums    

print(factroiral(5))
    

