class Solution:
    def Binary_search(self,arr,target,low,high):
        if low>high:return -1
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            return self.Binary_search(arr,target,mid+1,high)
        else:
            return self.Binary_search(arr,target,low,mid-1)

nums=list(map(int,input("Enter the numbers:").split()))
x=int(input())
a=Solution()
ind=a.Binary_search(nums,x,0,len(nums)-1)
print(ind)