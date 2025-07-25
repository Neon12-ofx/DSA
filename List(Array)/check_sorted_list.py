def check_sorted_list(arr):
    for i in range(0,len(arr)-1):
        if(arr[i]>arr[i+1]):
            return False

    return True

n=list(map(int,input().split()))
print(check_sorted_list(n))