nums=input("Enter two values:")
x,y=nums.split()
print(x,y)
arr=[[0 for i in range(int(y))] for j in range(int(x))]
print(arr)

for i in range(int(x)):
    for j in range(int(y)):
        arr[i][j]=i*j
print(arr)
