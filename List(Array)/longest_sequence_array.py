def longest_sequence_array(arr):
    my_set = set(arr)
    for i in range (0,len(arr)):
        my_set.add(arr[i])
    longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x=x+1
            longest=max(longest,count)
    return longest

print(longest_sequence_array(list(map(int,input().split()))))
