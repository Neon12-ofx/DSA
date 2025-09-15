def combination_sum_iii(index,total,numbers,subset,result):
    if total == 0 and len(subset)==3:
        result.append(subset.copy())
        return
    if index >= len(numbers):
        return
    if total <0:
        return
    for i in range(index,len(numbers)):
        if i>index and numbers[i] == numbers[i-1]:
            continue
        subset.append(numbers[i])
        Sum=total-numbers[i]
        combination_sum_iii(i+1,Sum,numbers,subset,result)
        subset.pop()
    return result
print(combination_sum_iii(0,9,[1,2,3,4,5,6,7,8,9],[],[]))

