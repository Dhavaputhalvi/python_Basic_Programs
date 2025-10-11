num=int(input("enter sequence end: "))
a=0
b=1
print(a,b)
for i in range(1,num-1):
    c=a+b
    a=b
    b=c
    print(b)
