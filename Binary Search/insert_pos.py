def insert_pos(s,target):
    n=len(s)
    lb=n
    l=0
    h=n-1

    while l<=h:
        mid=(l+h)//2
        if s[mid]>=target:
            lb=mid
            h=mid-1
        else:
            l=mid+1
        #print(s[l],s[h],s[mid])
    return lb

n=list(map(int,input().split()))
target=int(input())
print(insert_pos(n,target))
