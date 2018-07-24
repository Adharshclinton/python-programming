n=input()
if n>1:
 for i in range(2, n):
   if ((n%i)==0):
	   print("no it is not a prime number")
	   break:
   else:
	   print("yes it is a prime number")
else:
  print("no it is not a prime number")
