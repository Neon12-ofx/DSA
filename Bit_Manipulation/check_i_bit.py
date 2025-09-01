def check_i_bit(x:int,i)->bool:
    num=list(con2Bin(x))
    num_l=len(num)
    if num[i]=="1":
        return True
    return False



def con2Bin(num: int) -> str:
    # 13->1101
    result = " "
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    result = result[::-1]
    return result

print(check_i_bit(13,1))