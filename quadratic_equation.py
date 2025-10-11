import math
a=int(input("enter coefficient of a:"))
b=int(input("enter coefficient of b:"))
c=int(input("enter coefficient of c:"))
determinant=(b**2)-(4*a*c)
print(determinant)
if determinant==0:
    print("helo")
    root=(-b)/(2*a)
    print("the root is:",root)
elif determinant>0:
    print("HiI")
    root1=(-b+(math.sqrt(determinant)))/(2*a)
    root2=(-b-(math.sqrt(determinant)))/(2*a)
    print("the roots are:",root1,root2) 
else:
    root=(-b)/(2*a)
    imaginaryPart=math.sqrt(abs(determinant))
    print("Root: ",root," Imaginary part: ",imaginaryPart,"i")
