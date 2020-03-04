class calculator:
    def __int__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        c=a+b
        print(c)
    def subtract(self):
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        c=a-b
        print(c)
    def multiply(self):
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        c=a*b
        print(c)
    def divide(self):
        a=int(input("enter the first number: "))
        b=int(input("enter the second number: "))
        c=a/b
        print(c)
a1=calculator()
print("Press A to add \nPress s to subtract \nPress m to multiply \nPress d to divide")
while True:
    a=input("Enter your choice")
    if a=='s'or a=='S':
        x=a1.subtract()
    elif(a=='a' or a=='A'):
        x = a1.add()
    elif(a=='M' or a=='m'):
        x = a1.multiply()
    elif(a=="d" or a=="D"):
        x = a1.divide()
    else:
        print("invalid character")
        break

