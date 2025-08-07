def floor_and_ceil(arr,target):
    floor=-1
    ceil=-1
    l=0
    h=len(arr)-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]==target:
            return [arr[mid],arr[mid]]
        elif arr[mid]>target:
            ceil=arr[mid]
            h=mid-1
        else:
            floor=arr[mid]
            l=mid+1
    return [floor,ceil]

nums=list(map(int,input().split()))
x=int(input())
print(floor_and_ceil(nums,x))

