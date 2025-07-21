def opti_sort(arr):
    s=len(arr)
    for i in range(s-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_swap=True
        if (is_swap==False):
            break
    return arr

n=list(map(int,input().split()))
print("sorting using Optimized Bubble Sort:",opti_sort(n))