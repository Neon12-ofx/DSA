# def right_rotate_slice(arr):
#     n = len(arr)
#     arr[:]=str(arr[-1])+str(arr[0:n-1])
#     return arr
#
# n=list(input().split())
# print(right_rotate_slice(n))

def right_rotate_slice(arr):
    n = len(arr)
    if n == 0:
        return arr
    arr[:] = [arr[-1]] + arr[0:n-1]
    return arr

n = input().split()
print(right_rotate_slice(n))
