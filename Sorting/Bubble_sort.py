def Bubble_sort(arr):
    s=len(arr)
    for i in range(s-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


n=list(map(int,input().split()))
print("Sorted array",Bubble_sort(n))