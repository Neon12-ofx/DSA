# def sum_no(i,n,s=0):
#     if(i>n):
#         print(s)
#         return
#     sum_no(i+1,n,s+i)
#
# a,b=int(input()),int(input())
# sum_no(a,b,0)

def sum_f(n):
    if n==1:
        return 1
    return n+sum_f(n-1)

n=int(input())
print(sum_f(n))
