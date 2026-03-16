# Input: 5
# Output:
# 1 2 3 4 5

def printNumber(n):
    if n == 0:
        return
    printNumber(n-1)
    print(n)

printNumber(5)  
    


# Input: 5
# Output: 15

def sumOfN(n):
    if(n==0):
        return 0
    else:
        return n+sumOfN(n-1)
    
# Input: "hello"
# Output: "olleh"   

def reverse(string):
    if(string==""):
        return ""
    else:
        return string[1:]+string[0]
print(reverse("hello"))    

#input 121
#output true
# check plaindrome number using recursion

def is_palindrome(number):
    string=str(number)
    if len(string)<=1:
        return True
    if(string[0]!=string[-1]):
        return False
    else:
        return is_palindrome(string[1:-1])
print(is_palindrome(121))