def rotate_2d(matrix):
    r=len(matrix)
    c=len(matrix[0])


    result=[[0]*r for _ in range(c)]

    for i in  range(r):
        for j in range(c):
            result[j][(r-1)-i]=matrix[i][j]
    return result

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate_2d(matrix)
print(rotate_2d(matrix))