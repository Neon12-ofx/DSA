def lower_b(arr,target):
    #[1 1 1 2 3 3 3 5 6 7 7 7 9 12 12 13]
    n=len(arr)
    lb = n
    l=0
    h=n-1
    while l<=h:
        m=(l+h)//2
        if arr[m]>=target:   #codn for arr[m]>=target
            lb=m  #store the lowest index
            h=m-1
        else:
            l=m+1
    return lb

n=list(map(int,input().split()))
x=int(input())
print(lower_b(n,x))