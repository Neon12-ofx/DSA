def count_all_subsequence_sum(arr,ind,total,target):
    count=0
    if total == target:
        return 1
    if ind >= len(arr):
        return 0
    if total > target:
        return 0

    sum= total+arr[ind]
    left=count_all_subsequence_sum(arr,ind+1,sum,target)
    sum= total
    right=count_all_subsequence_sum(arr,ind+1,sum,target)
    return left+right

print(count_all_subsequence_sum([5,9,4],0,0,9))