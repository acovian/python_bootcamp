def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    print(first_letter.upper() + inbetween + fourth_letter.upper() + rest)

old_macdonald('macdonald')
