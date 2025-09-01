def con2Bin(num:int)->str:
    #13->1101
    result=" "
    while num>0:
        if num%2==1:
            result +="1"
        else:
            result += "0"
        num=num//2
    result=result[::-1]
    return result

print(con2Bin(13))
print(con2Bin(100))
