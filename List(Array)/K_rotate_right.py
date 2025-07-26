def right_rotate(arr,k):
    n=len(arr)
    while k!=0:
        temp=arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i+1]=arr[i]
        arr[0]=temp
        k-=1
        print(arr)
    return arr

n=list(map(int,input().split()))
x=int(input())
print(right_rotate(n,x))