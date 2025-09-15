def binary_st(index,flag,numbers,result):
    if index >= len(numbers):
        result.append("".join(numbers))
        return
    numbers[index]="0"
    binary_st(index+1,True,numbers,result)
    if flag == True:
        numbers[index]="1"
        binary_st(index+1,False,numbers,result)
        numbers[index]="0" #backtracking cond


def generate_binary(n):
    numbers=["0"]*n
    result=[]
    binary_st(0,True,numbers,result)
    return result

print(generate_binary(2))