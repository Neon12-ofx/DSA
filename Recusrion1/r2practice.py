#print x , n times
# def func(x,n):
#     if(n==0):
#         return
#     print(x)
#     func(x,n-1)
# f,a=int(input()),int(input())
# func(f,a)

#print 1 to N in reverse(head Recursion)
# def fun(n):
#     if(n==0):
#         return
#     print(n)
#     fun(n-1)
# x=int(input())
# fun(x)

#print 1 to N in forward(Tail recursion)
# def fun(n):
#     if(n==0):
#         return
#     fun(n-1)
#     print(n)
# x= int(input())
# fun(x)

#print i to N
def fun(i,n):
    if(i>n):
        return
    print(i)
    fun(i+1,n)
f,a=int(input()),int(input())
fun(f,a)