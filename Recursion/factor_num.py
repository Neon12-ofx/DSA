from math import sqrt
#brute force
def b_factor_no(n):
    count=[]
    for i in range(1,n+1):
        if(n%i==0):
            count.append(i)
    return count

#better soln
def be_factor_no(n):
    count=[]
    for i in range(1,n//2):
        if(n%i==0):
            count.append(i)
    count.append(n)
    return count

#optimal soln
def op_factor_no(n):
    count=set()
    for i in range(1,int(sqrt(n))+1):
        if(n%i==0):
            count.add(i)
            count.add(n//i)
    return sorted(count)


num=int(input("Enter the NUmber:"))
print(num)
result=b_factor_no(num)
result1=be_factor_no(num)
result2=op_factor_no(num)
print(f"The factor for {num} by optimal soln is {result2}")
print(f"The factor for {num} by better soln is {result1}")
print(f"The factor of {num} by Brute force is {result}")

