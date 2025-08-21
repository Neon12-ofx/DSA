def mark_infi(matrix,row,col):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        if matrix[i][c]!=0:
            matrix[i][c]=float("inf")

    for j in range(c):
        if matrix[r][j]!=0:
            matrix[r][j]=float("inf")

    return matrix

def set_zero(matrix):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                matrix[i][j]=mark_infi(matrix,i,j)

    for i in range(r):
        for j in range(c):
            if matrix[i][j]==float("inf"):
                matrix[i][j]=0
    return matrix

mat=map(int,input().split())
print(set_zero(mat))