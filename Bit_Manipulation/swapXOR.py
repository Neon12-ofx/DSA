def swapXor(a,b):
    a=a^b
    b=a^b
    a=a^b

    return a,b

print(swapXor(11,10))