n1= int(input("Enter 1st number : "))
n2= int(input("Enter 2nd number : "))
n3= int(input("Enter 3rd number : "))
if(n1>n2 and n1>n3):
 print( "{0} is greater number than {1} and {2}".format(n1,n2,n3))
elif(n2>n3 and n2>n1):
 print("{0} is greater number than {1} and {2}".format(n2,n3,n1))
else:
 print("{0} is greater number than {1} and {2}".format(n3,n1,n2))
