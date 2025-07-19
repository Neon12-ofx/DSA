import math
n=int(input("Enter the Number"))
num=n
nod=len(str(n))
total = 0
while(num>0):
    last_digit=num%10
    total=total+pow(last_digit,nod)
    num=num//10

if(total==n):
    print("Armstrong_No")
else:
    print("not_Armstrong_No")