#5 10 -3 -1 -10 6
#5 -3 10 -3 6 -10
def opti_Rearrange_element(arr):
    n=len(arr)
    result=[0]*n
    pos_ind,neg_ind=0,1
    for i in range(n):
        if arr[i]>0:
            result[pos_ind]=arr[i]
            pos_ind+=2
        else:
            result[neg_ind]=arr[i]
            neg_ind+=2
    return result


n=list(map(int,input().split()))
print(opti_Rearrange_element(n))