import math

def greedy_money_exchange(denom, amount):
    i = 0
    used = [0]*len(denom)
    while(amount>0):
        num = math.floor(amount/denom[i])
        used[i] = num
        amount = amount-num*denom[i]
        i = i + 1
    return used
