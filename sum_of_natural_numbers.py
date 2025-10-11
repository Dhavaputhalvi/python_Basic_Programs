num=int(input("enter a number: "))
sum=0
for i in range(1,num+1):
    sum+=i
for i in range(1,num):
    print(f"{i}+")
print(num,"=",sum)
