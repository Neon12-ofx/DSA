def remove_element(arr,x):
    i=0
    n=len(arr)
    if n==0:
        return arr

    while i<n:
        if arr[i]==x:
            break
        i=i+1

    if i==n and x not in arr:
        return arr

    j=i+1
    while j<n:
        if arr[j]!=x:
            arr[i]=arr[j]
            i+=1
        j+=1
    return i

n=list(map(int,input().split()))
x=int(input())
print(remove_element(n,x))