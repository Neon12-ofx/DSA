n=list(map(str,input().strip()))
m=list(map(str,input().strip().split()))
hash_st={}
num_len=len(n)
for i in range(0,num_len):
    hash_st[n[i]]=hash_st.get(n[i],0)+1
print(hash_st)

for i in m:
    print(f"The Freq of {i} is : {hash_st.get(i,0)}")
