def myfunc(string):
    newstr = ""
    for i in string:
        thing = string.index(i)
        if thing%2==0:
            newstr+=(i.upper())
        else:
            newstr+=(i)
    print (newstr)

myfunc('Anthropomorphism')
