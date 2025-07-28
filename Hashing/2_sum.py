def two_sum(arr,tar):
    #BY USING THE HASSH MAP
    n=len(arr)
    s={}
    for i in range(n):
        diff=tar-arr[i]
        if diff in s:
            return [s[diff],i]
        s[arr[i]]=i

x=list(map(int,input().split()))
y=int(input())
print(two_sum(x,y))