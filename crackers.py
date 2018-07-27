# def animal_crackers(str1, str2):
#     if str1[0] == str2[0]:
#         print('True')
#     else:
#         print('False')
#
# animal_crackers('Hippo', 'Monkey')

def animal_crackers(text):
    wordlist = text.lower().split()

    first = wordlist[0]
    second = wordlist[1]

    return first[0] == second[0]

animal_crackers('Levelheaded Llama')
