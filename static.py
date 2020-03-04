import cal
print("Calculator")
print("***********")
print("Press A to add \nPress s to subtract \nPress m to multiply \nPress d to divide")
a=input("enter your choice :")
if a=='A' or a=='a':
    cal.add()
elif(a=='s' or a=='S'):
    cal.subtract()
elif(a=='M' or a=='m'):
    cal.multiply()
elif(a=='d' or a=="D"):
    cal.divide()
else:
    print("enter valid option")








