def selection_sort(arr):
    n=len(arr)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        #print(arr)
    return arr

s=list(map(int,input().split()))
print("sorting using Selection Sort:",selection_sort(s))