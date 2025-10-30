def generator(n):
        if n%7==0:
            print(n)

num=int(input("Enter sequence end such as 100"))
for i in range(num):
    generator(i)
