def max_consec_one(arr):
    n=len(arr)
    c=0
    max_c=0
    i=0
    while i<n:
        if arr[i]==1:
            c+=1
            max_c=max(max_c,c)
        else:
            c=0
        i+=1
    return max_c

n=list(map(int,input().split()))
print(max_consec_one(n))


