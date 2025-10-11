matrix1=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        result[i][j]=matrix1[j][i]
print(result)
