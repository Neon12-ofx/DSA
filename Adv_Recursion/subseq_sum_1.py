def subseq_sum(index,total,numbers):
    if index>=len(numbers):
        return [total]
    Sum=total+numbers[index]
    pick=subseq_sum(index+1,Sum,numbers)
    Sum=total
    n_pick=subseq_sum(index+1,Sum,numbers)
    return pick + n_pick

print(subseq_sum(0,0,[5,9,3]))