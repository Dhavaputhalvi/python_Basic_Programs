num=int(input("enter a number: "))
string=str(num)
length=len(string)
sum=0
tnum=num
for i in string:
    print(i)
    digit=tnum%10
    sum+=(digit**length)
    tnum=tnum//10

if(sum==num):
    print("armstrong Number ")
else:
    print(" not a armstrong Number ")
