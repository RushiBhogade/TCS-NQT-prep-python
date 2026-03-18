#matrix problem 90% rotate
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# for i in range(len(matrix)):
#     for j in range(i,len(matrix)):
#         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
# for rows in matrix:
#     rows.reverse()
# print(matrix)

#matrix transpose 180 degree

matrix.reverse()
for rows in matrix:
    rows.reverse()
# for i in range(len(matrix)):
#     matrix[i].reverse()
    
print(matrix)

#matrix transpose 270 degree
for i in range(len(matrix)):
    for j in range(i,len(matrix)):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for j in range(len(matrix)):
    top=0
    bottom=len(matrix)-1
    while top <bottom:
        matrix[top][j],matrix[bottom][j]=matrix[bottom][j],matrix[top][j]
        top+=1
        bottom-=1
print(matrix)        

