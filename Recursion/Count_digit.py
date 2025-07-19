import math
num=int(input("Enter the number:"))
print(num)
n=num
count=0
while(num>0):
    last_digit=num%10
    count=count+1
    print(last_digit)
    num=num//10
print(f"the length:{count}")

s=int(math.log10(n)+1)
print(s)