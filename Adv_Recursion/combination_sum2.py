def Combination_sum_two(index,total,numbers,subset,target):
    result=set()
    if total == target:
        sub=sorted(subset)
        result.add(tuple(sub))
        return result
    if index >= len(numbers):
        return set()
    if total>target:
        return set()

    subset.append(numbers[index])
    Sum = total + numbers[index]
    pick = Combination_sum_two(index+1,Sum,numbers,subset,target)
    subset.pop()
    Sum= total
    not_pick=Combination_sum_two(index+1,Sum,numbers,subset,target)
    return pick | not_pick

print(Combination_sum_two(0,0,[1,1,2,1,2],[],4))