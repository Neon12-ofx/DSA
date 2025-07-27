#nums=[1,0,3,4]
#length 4 means n=[0 to 4], n=[0,1,2,3,4]
'''def missing_no(arr):
    n=len(arr)
    for i in range(0,n+1):
        if i not in arr:
            return i    #missing term'''

#dictionary using hashing
# def better_missing_no(arr):
#     d={}
#     n=len(arr)
#
#     for i in range(0,n+1):
#         d[i]=0
#
#     for i in arr:
#         d[i]=1
#
#     for k,v in d.items():
#         if v==0:
#             return k

def opti_missing_no(arr):
    n=len(arr)
    s=0
    total = int(n * (n + 1) / 2)
    for i in range(0,n):
        s=s+arr[i]

    return total-s


n=list(map(int,input().split()))
#print(missing_no(n))
#print(better_missing_no(n))
print(opti_missing_no(n))
