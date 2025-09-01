def solve(nums,ind,subset,target):
    result=[]
    if ind >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
        return result

    subset.append(nums[ind])
    result += solve(nums,ind+1,subset,target)
    subset.pop()
    result += solve(nums,ind+1,subset,target)
    return result

print(solve([1,2,3,4],0,[],5))