def backtract(arr,ind,total,subset,target):
    result=[]
    if total == target:
        result.append(subset.copy())
        return result
    if total > target:
        return []
    if ind >= len(arr):
        return []

    subset.append(arr[ind])
    Sum=total+arr[ind]
    result+=backtract(arr,ind+1,Sum,subset,target)
    e=subset.pop()
    Sum=total
    result+=backtract(arr,ind+1,Sum,subset,target)
    return result

print(backtract([5,9,4],0,0,[],9))