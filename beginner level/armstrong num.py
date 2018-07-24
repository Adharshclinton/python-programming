a=int(raw_input())
s = 0
t = n
while (t > 0):
       digit = temp % 10
       s =s+ digit ** 3
       t /= 10
if (n == s):
       print("armstrong number")
else:
       print("not an armstrong number")
