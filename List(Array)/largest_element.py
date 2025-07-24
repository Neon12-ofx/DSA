def large(arr):
    largest=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

n=list(map(int,input().split()))
print("Largest element:",large(n))
