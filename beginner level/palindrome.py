number=int(raw_input("Enter the number"))
n1=num
n=0
while(number>0):
        d=number%10
        n=n*10+d
        number=number/10
if(n==n1):
        print("It is a palindrome")
else:
        print("It is  not a palindrome")
