n=list(map(int,input().split()))
m=list(map(int,input().split()))

hash_dict={}
num=len(n)

#n list ko tranvese karke uska freq pre store kiya
for i in range(0,num):
    hash_dict[n[i]]=hash_dict.get(n[i],0)+1
print(hash_dict)

#m list ke element ko find karke uska freq linkhunga
for i in m:
    # if i<1 or i>num:
    #     print(f"The freq of {i} is : {0}")
    # else:
    #     print(f"The freq of {i} is : {hash_dict[i]}")
    print(f"The Freq of {i} is : {hash_dict.get(i,0)}")