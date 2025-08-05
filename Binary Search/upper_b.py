def upper_b(arr,target):
    n=len(arr)
    l=0
    h=n-1
    up=n
    while l<=h:
        m=(l+h)//2
        if arr[m]>target:
            up=m
            h=m-1
        else:
            l=m+1
        print(l,h)
    return up

nums=list(map(int,input().split()))
t=int(input())
print(upper_b(nums,t))