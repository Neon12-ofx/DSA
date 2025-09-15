def Combination_sum(index,total,numbers,subset,target):
    result=[]
    if total == target:
        result.append(subset.copy())
        return result
    if index >= len(numbers):
        return []
    if total>target:
        return []

    subset.append(numbers[index])
    Sum = total + numbers[index]
    pick = Combination_sum(index,Sum,numbers,subset,target)
    subset.pop()
    Sum= total
    not_pick=Combination_sum(index+1,Sum,numbers,subset,target)
    return pick + not_pick

print(Combination_sum(0,0,[2,3,6,7],[],7))
