n=list(map(int,input().split()))
m=list(map(int,input().split()))

#here we makinf a list where we are pre storing the value in index later to acccessing easily
hash_list=[0]*(len(n)+1)
for num in n:
    hash_list[num]+=1 #increasing the frequencies

for num in m:
    if num<1 or num>len(n):
        print(0)
    else:
        print(f"The freq of {num} is :{hash_list[num]}")