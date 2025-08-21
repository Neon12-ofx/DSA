nums=[[1,2,3],[4,5,6],[7,8,9]]
row=len(nums)
col=len(nums[0])

result=[[0]*row for _ in range(col)]

for i in range(0,row):
    for j in range(0,col):
        result[j][i]=nums[i][j]
        print(result,end=" ")
    print()