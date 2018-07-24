a=int(raw_input())
b=int(raw_input())
 
for n in range(a,b):
   s = 0
   t = n
   while t > 0:
       digit = t % 10
       s =s+ digit ** 3
       t /= 10
 
   if n == s:
       print(n)
