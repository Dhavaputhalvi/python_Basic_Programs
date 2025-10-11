def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

num1=int(input("Enter  number 1:"))
num2=int(input("Enter  number 2:"))

print("Select operation:\n 1.Addition\n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit")
n=int(input("Enter  choice:"))
match n:
    case 1:
        result=add(num1,num2)n
        print(result)
    case 2:
        result=sub(num1,num2)
        print(result)
    case 3:
        result=mul(num1,num2)
        print(result)
    case 4:
        if num2==0:
            raise ValueError(" division by zero")
        else:
            result=div(num1,num2)
            print(result)
    case 5:
        exit(0)
    case _:
        print("enter number between 1 to 5")
