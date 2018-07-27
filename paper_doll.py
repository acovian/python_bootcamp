def paper_doll(text):
    result = ''

    for char in text:
        result += char*3
    print(result)

paper_doll('Mississippi')
