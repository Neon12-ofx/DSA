def opti_moving(arr):
    n = len(arr)
    i=0
    if n==1:            #if array has only one lenght arr=[1]
        return arr

    while i<n:
        if arr[i]==0:
            break       #if 0 is found stop it at that index dont move the i
        i+=1            #if not move i = i+1 index

    if i==n:            #if array has no element zero
        return arr
    j=i+1
    while(j<n):
        if arr[j] != 0: #CHECKING FOR UNIQUE NO
            arr[i],arr[j]=arr[j],arr[i] #SWAPPING THEM WITH ZERO AND MOVING THEM FORWARD
            i+=1
        j+=1
    return arr

n=list(map(int,input().split()))
print(opti_moving(n))