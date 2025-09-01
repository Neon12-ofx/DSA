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

def comp2s(x:str)->str:
    return ""

comp2s("1011")
