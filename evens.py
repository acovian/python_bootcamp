def lesser_of_two_evens(num1, num2):
    if num1%2==0 and num2%2==0:
        if num1 > num2:
            print(num2)
        else:
            print(num1)
    else:
        if num1 > num2:
            print(num1)
        else:
            print(num2)

lesser_of_two_evens(2,5)
