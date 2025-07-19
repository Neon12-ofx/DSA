num=list(map(int,input("Enter the list").split()))
print(num)
f_map={}
for i in range(0,len(num)):
    if num[i] in f_map:
        f_map[num[i]] +=1
    else:
        f_map[num[i]]=1

print(f_map)