# 5 10 -3 -1 -10 6
def rearrange_element(arr):
    pos=[]
    neg=[]

    #seperating the array into 2
    for i in range(len(arr)):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])

    for i in range(0,len(pos)):
        arr[2*i]=pos[i]
        arr[2*i+1]=neg[i]
    return arr

n=list(map(int,input().split()))
print(rearrange_element(n))