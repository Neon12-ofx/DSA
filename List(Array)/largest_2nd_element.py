def largest_2nd_element(arr):
    largest=float('-inf')
    s_largest=float('-inf')
    for i in range(0,len(arr)):
        if arr[i]>=largest:
            s_largest=largest
            largest=arr[i]
        elif arr[i]>s_largest and arr[i] != largest:
            s_largest=arr[i]
    return s_largest

n=list(map(int,input().split()))
print(largest_2nd_element(n))