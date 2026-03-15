n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(n,m))