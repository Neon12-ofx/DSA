#Brute for tc-->O(N^2)
def maxi_sub_sum(arr):
    maxi=float('-inf')
    for i in range(0,len(arr)):
        total = 0   #Each time you start a new subarray from index i, you need a fresh total.
                    # If you don’t reset total, then it will keep accumulating values from previous subarrays, which gives incorrect results.
        for j in range(i,len(arr)):
            total=total+arr[j]
            maxi=max(maxi,total)
    return maxi

n=list(map(int,input().split()))
print(maxi_sub_sum(n))
