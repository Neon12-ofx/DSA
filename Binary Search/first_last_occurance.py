def first_last_occ(nums,target):
    def lbound(nums,target):
        low=0
        high=len(nums)-1
        lb=-1
        while(low<=high):
            mid=(low+high)//2
            # if nums[mid]==target:
            #     lb=mid
            #     high=mid-1
            if nums[mid]>=target:
                lb = mid
                high=mid-1
            else:
                low=mid+1
        return lb

    def upbd(nums,target):
        low=0
        high=len(nums)-1
        ub=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ub=mid
                l=mid+1
            if nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return ub

    lb=lbound(nums,target)
    ub=upbd(nums,target)
    return [lb,ub]


nums=list(map(int,input().split()))
x=int(input())
print(first_last_occ(nums,x))