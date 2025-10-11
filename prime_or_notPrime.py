n=int(input("Enter a a number"))
flag=False
if n==1:
    print(f"{n} is not a prime number")
elif n>1:
    for i in range(2,n):
        if(n%i==0):
            flag=True
            break
else:
    print("enter positive number")




if(flag==True):
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
