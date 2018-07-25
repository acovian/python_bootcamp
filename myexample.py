st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

for num in range(0,11,2):
        print (num)

[x for x in range(1,51) if x%3 == 0]

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word)
