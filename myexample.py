st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

for num in range(0,11):
    if num % 2 == 0:
        print (num)
