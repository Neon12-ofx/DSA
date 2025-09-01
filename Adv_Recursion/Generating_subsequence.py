def solve(num,ind,subset):
    result=[]
    if ind>=len(num):
        result.append(subset.copy())
        return result
    subset.append(num[ind])
    result+=solve(num,ind+1,subset)
    subset.pop()
    result+=solve(num,ind+1,subset)
    return result

print(solve([1,2,3],0,[]))