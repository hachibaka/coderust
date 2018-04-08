def MaxProfit_recursive(a,left=0,right=None):
    if not right:
        right = len(a)
    if right - left <=1:
        return 0
    mid = (left+right)//2
    result = max(a[mid:right]) - min(a[left:mid])
    return max(result,
               MaxProfit_recursive(a,left,mid),
               MaxProfit_recursive(a,mid,right))


def MaxProfit_kadane(a):
    current_buy  = a[0]
    current_profit = -1
    global_sell = a[1]
    global_profit = global_sell - current_buy
    for i in range(1,len(a)):
        current_profit = a[i] - current_buy
        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = a[i]
        if a[i] < current_buy:
            current_buy = a[i]
    return global_profit


a1 = [7, -1, 8, 10, 5, -7, 24]
a2 = [21,12,11,9,6,3]
print(MaxProfit_recursive(a1))
print(MaxProfit_kadane(a1))
print(MaxProfit_recursive(a2))
print(MaxProfit_kadane(a2))
