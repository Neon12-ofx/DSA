#[7 2 1 5 6 4 8]
def buy_and_sell(arr):
    max_profit = 0
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                profit=arr[j]-arr[i]
                max_profit=max(max_profit,profit)
    return max_profit

n=list(map(int,input().split()))
print(buy_and_sell(n))
