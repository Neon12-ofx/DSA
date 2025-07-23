def Merge_arr(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    #print(result)
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2

    L_arr=arr[:mid]
    R_arr=arr[mid:]

    left=merge_sort(L_arr)
    right=merge_sort(R_arr)
    return Merge_arr(left,right)

n=list(map(int,input().split()))
print("Sorted array:",merge_sort(n))

