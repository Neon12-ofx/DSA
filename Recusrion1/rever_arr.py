def reverse_in(left,right,num):
    if left>=right:
        return num
    num[left],num[right]=num[right],num[left]
    return reverse_in(left+1,right-1,num)

n=list(map(int,input().split()))
l,r=int(input()),int(input())
print(reverse_in(l,r,n))
