import math
C=50
H=30
num=input("Enter 3 values for c:")
num1=num.split(",")
print(num1)  
for i in num1:
     i=int(i)
     print(i)
     print(math.sqrt((2*C*i)/H))
