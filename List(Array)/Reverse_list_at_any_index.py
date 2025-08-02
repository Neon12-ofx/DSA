def reverse_at_any_index(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

n=list(map(int,input().split()))
x,y=int(input()),int(input())
print(reverse_at_any_index(n,x,y))
