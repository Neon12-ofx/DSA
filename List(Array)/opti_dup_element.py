def opti_dup_element(arr):
    n=len(arr)
    if n==1:
        return 1
    i=0
    j=i+1
    while j<n:
        if arr[j]!= arr[i]:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
        j+=1
    return i+1
print(opti_dup_element([1,1,2,3,3,4,4,4,5]))