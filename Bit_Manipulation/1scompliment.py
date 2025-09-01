def comp1s(x:str)->str:
    lis_x=list(x)
    index=len(lis_x)-1
    while index>=0:
        if lis_x[index]=="0":
            lis_x[index]="1"
        else:
            lis_x[index]="0"
        index-=1
    return "".join(lis_x)

print(comp1s("1101"))
print(comp1s("1011"))
