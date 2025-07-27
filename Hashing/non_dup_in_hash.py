def non_dup(arr):
    h_list=[0]*(len(arr)+1)
    for i in arr:
        h_list[i]+=1

    for i in range(len(h_list)):
        if h_list[i] == 1:
            return i
    return 0

def non_dup_dic(arr):
    d={}
    for i in range(0,len(arr)):
        d[arr[i]]=d.get(arr[i],0)+1
    for i in d:
        if d[i]==1:
            return i
    return 0


n=list(map(int,input().split()))
print(non_dup(n))
print(non_dup_dic(n))
