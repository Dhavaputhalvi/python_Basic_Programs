matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[2,3,4],[4,3,6],[7,9,0]]
result=[]
for i in range(0,3):
    row=[]
    for j in range(0,3):
       row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)
print(result)
