nums=[[1,2,3],[4,5,6],[7,8,9]]
row=len(nums)
col=len(nums[0])
for i in range(0,row):
    for j in range(0,col):
        print(nums[i][j], end=" ")
    print()