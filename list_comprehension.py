mylist = [x for x in range(0,11) if x%2==0]
print(mylist)

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print (results)
