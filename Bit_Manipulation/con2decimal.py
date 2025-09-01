def con2Decimal(x:str)->int:
    #1101->13
    result = 0
    power =0
    index=len(x)-1
    while index>=0:
        num = int(x[index])*(2**power)
        result += num
        power += 1
        index -= 1
    return result

print(con2Decimal("1101"))
print(con2Decimal("1011"))