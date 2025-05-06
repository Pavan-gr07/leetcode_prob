def bestTimeBuySell(arr):
    buy = arr[0] 
    profit = 0
    for ele in arr:
        profit = max(profit,ele-buy)
        buy = min(buy,ele)
    return profit

print(bestTimeBuySell([7,1,5,3,6,4]))