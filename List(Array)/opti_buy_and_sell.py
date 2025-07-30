def opti_buy_and_sell(arr):
    max_profit=0
    min_profit=float('inf')
    for i in range(len(arr)):
        min_profit=min(min_profit,arr[i])
        profit=arr[i]-min_profit
        max_profit=max(max_profit,profit)
    return max_profit

n=list(map(int,input().split()))
print(opti_buy_and_sell(n))