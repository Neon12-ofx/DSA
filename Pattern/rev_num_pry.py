# 11 12 13 14 15
# 10 9 8 7
# 4 5 6
# 2 3
# 1
c=16
for i in range(5,0,-1):
    for j in range(1,i+1):
        c=c-1
        print(c,end=" ")
    print()