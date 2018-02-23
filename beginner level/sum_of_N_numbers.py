num =int(input("enter the number:"))
if num < 0:
   print("Enter a positive number")
else:
   total= 0
   while(num > 0):
       total += num
       num -= 1
   print("The sum of natural numbers is %d"%total)
