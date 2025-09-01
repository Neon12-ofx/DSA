def backtract(nums,ind,total,subset,target):
    result=[]
    if total == target:
        result.append(subset.copy())
        return True
    if total > target:
        return False
    if ind >= len(nums):
        return False
    subset.append(nums[ind])
    Sum=total+nums[ind]
    pick=backtract(nums,ind+1,Sum,subset,target)
    if pick==True:
        return True
    Sum=total
    n_pick=backtract(nums,ind+1,Sum,subset,target)
    return n_pick


print(backtract([5,9,4],0,0,[],6))
