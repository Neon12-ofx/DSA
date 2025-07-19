import math
def m_count_digits(n):
    return int(math.log10(n)+1)

num = int(input("enter number"))
a=num
print(num)
while num>0:
    last_digit=num%10
    print(last_digit)
    num=num//10
s=m_count_digits(a)
print(f"the no of digit:{s}")