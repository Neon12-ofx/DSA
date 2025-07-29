#[-1,2,-3,4,5]
#KADANE's Algorithm
#t(c)-->O(n)

def opti_maximum_sum_subarr(arr):
    n=len(arr)
    total=0
    maxi=float('-inf')
    for i in range(0,n):
        total+=arr[i]
        maxi=max(maxi,total)
        if (total<0):
            total=0
    return maxi

x=list(map(int,input().split()))
print(opti_maximum_sum_subarr(x))