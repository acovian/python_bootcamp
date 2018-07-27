# def master_yoda(string1):
#     a = string1.split()
#     a.reverse()
#     result = " ".join(a)
#     print(result)

def master_yoda(text):
    wordlist = text.split()
    reverse_word_list = wordlist[::-1]
    print( ' '.join(reverse_word_list).lower() )

master_yoda('We are ready')
