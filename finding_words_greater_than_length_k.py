string=str(input("Enter a string:"))
default_length=5
arr=string.split(" ")
print(string)
for i in arr:
    if len(i)>default_length:
        print(i)
    else:
        print("not greater")
