num=list(map(int,input().split()))
hash_map={}
n=len(num)
for i in range(0,n):
    hash_map[num[i]]=hash_map.get(num[i],0)+1
    #so hash[num[0]]=hash.get(num[0],0)+1
    #means if num[0]=1 hash[1]=hash.get(1,0)+1
    #if in hash dict if 1 is present it will return that value or freq if not then 0 will be give as values then 1 is added
print(hash_map) 