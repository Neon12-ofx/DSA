def moving_zeros_to_end(arr):
    n=len(arr)
    temp=[]
    for i in range(0,n):
        if arr[i]!=0:
            temp.append(arr[i])
    for i in temp:
        arr[i]=temp[i]
    for i in range(len(temp),n):
        arr[i]=0
    return arr
n=list(map(int,input().split()))
print(moving_zeros_to_end(n))