#arr1= [1,1,1,2,3,6,7]
#arr2=[1,2,3,4,4,5,6,7,8,9,12]
#res=[1,2,3,4,5,6,7,]
def merge(arr1,arr2):
    n=len(arr1)
    m=len(arr2)

    i,j=0,0
    res=[]
    while i<n and j<m:                      #i and j are two pointer traversing between two arr
        if arr1[i]<=arr2[j]:
            if len(res)==0 or res[-1]!=arr1[i]: #here we checking is len of res is 0 or the last element in res is similar to arr[i]
                res.append(arr1[i])
            i+=1
        else:
            if len(res)==0 or res[-1]!=arr2[j]:
                res.append(arr2[j])
            j+=1
    if i<n:                         #if arr have remaining left in arr1 is to move to res
        while i<n:
            if len(res)==0 or res[-1]!=arr1[i]:
                res.append(arr1[i])
            i+=1

    if j<m:
        while j<m:
            if len(res)==0 or res[-1]!=arr2[j]:
                res.append(arr2[j])
            j+=1
    return res

n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
print(merge(n1,n2))