def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        print(sum([a,b,c]))
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        print(sum([a,b,c])-10)
    else:
        print('BUST')

blackjack(5,6,7)
