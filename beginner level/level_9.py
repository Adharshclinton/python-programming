num= int(input("enter the number:"))
tot=0
if(num<=0):
	print("enter a positive number")
for i in range(1,num+1):
	tot=tot+i
print("the sum is %d" %tot)
