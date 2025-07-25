def duplicate_elements(arr):
    d={}
    n=len(arr)
    for i in range(0,n):
        d[arr[i]]=0 #we dont need value just the index
    print(d)
    c=0
    for j in d:
        arr[c]=j
        c=c+1
    return print("THE UNIQUE ELEMENT:",c)

n=list(map(int,input().split()))
duplicate_elements(n)
