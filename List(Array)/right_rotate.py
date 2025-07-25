def right_rotate(arr):
    n=len(arr)
    temp=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr

n=list(map(int,input().split()))
print(right_rotate(n))
