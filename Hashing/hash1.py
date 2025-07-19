n=list(map(int,input().split()))
m=list(map(int,input().split()))

for num in m: #num will tranverse in m list
    count=0 #now take count variable to count the freq of the no in n list
    for x in n: #x will traverse in n list
        if x==num: #this check if x no is present in m list if yes
            count+=1 #count increase of that x
    print(count) # print that count for that particular no
    #agian it exits then num will shift to next no