# Make a 2D array (list of lists)
array_2d = [
    [2, 5, 6, 6],
    [4, 3, 2, 2],
    [5, 6, 7, 3]
]

array_2d1 = [
    [2, 5, 1, 2],
    [4, 3, 2, 2],
    [5, 6, 7, 2],
    [4,3,2,2]
]

# multiplication 

def multiplication(a,b):
    col=len(a[0])
    rowa=len(a)
    rowb=len(b[0])
    result=[]
    # create Empty matrix
    if len(a[0]) != len(b):
        return "Multiplication not possible" 
    for _ in range(rowa):
        result.append([0]*rowb)

    for i in range(rowa):
        for j in range(rowb):
            for k in range(col):
                result[i][j] += a[i][k] * b[k][j]    
    return result

res=multiplication(array_2d,array_2d1)
print(res)

# addtion

def addtionOfmatrix(a,b):
    col=len(a[0])
    rowa=len(a)
    rowb=len(b[0])

    if(col!=rowb):
        return -1
    
    result=[]
    for _ in range(rowa):
        result.append([0]*rowb)
    for i in range(rowa):
        for j in range(rowb):
            result[i][j]+=a[i][j]+b[j][i]
    return result

res2 =addtionOfmatrix(array_2d,array_2d1)
print(res2,"addtion")


def subOfmatrix(a,b):
    rowa=len(a)
    col=len(a[0])
    rowb=len(b[0])

    if(rowb!=col):
        return -1
    result=[]
    for _ in range(rowa):
        result.append([0]*rowb)

    for i in range(rowa):
        for j in range(rowb):
            result[i][j] += a[i][j] - b[j][i]
    return result          
res3 = subOfmatrix(array_2d,array_2d1)
print(res3)

# rotate matrix only works for n * n

def Rotate90(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    for i in range(len(a)):
        a[i].reverse()
    return a
print(Rotate90(array_2d))

# 270
def Rotate270(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    a.reverse()
    return a
print(Rotate90(array_2d))

# 2180
def Rotate180(a):
    a.reverse()
    for rows in range(len(a)):
        a[rows].reverse()
    return a    

print(Rotate90(array_2d))
        









