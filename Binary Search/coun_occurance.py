def coun_occurance(arr,target):
    def lb_a(arr,target):
        lb=-1
        l=0
        h=len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>=target:
                lb=mid
                h=mid-1
            else:
                l=mid+1
        return lb
    def ub_a(arr,target):
        ub=-1
        l=0
        h=len(arr)-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]==target:
                ub=mid
                l=mid+1
            if arr[mid]>target:
                h=mid-1
            else:
                l=mid+1
        return ub
    lb=lb_a(arr,target)
    if lb==-1:
        return 0
    ub=ub_a(arr,target)
    return (ub-lb+1)

nums=list(map(int,input().split()))
target=int(input())
print(coun_occurance(nums,target))
