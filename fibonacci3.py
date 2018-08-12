def fib(N):
    if N == 1:
        return[1,0]
    else:
        terms = fib(N - 1)
        terms = [terms[0] + terms [1], terms[0]]
        return terms
def validate_positive_integer():
    while True:
        s = raw_input("Which term in the Fibonacci sequence you want to see? ")
        try:
            N = int(s)
            if N >= 500:
                print ("Enter a number smaller than 500")
            elif N > 0:
                return N
            else:
                print ("Enter a positive integer")
        except ValueError:
            print("Enter a positive integer")
def main():
    N = validate_positive_integer()
    print fib(N)[1]

if __name__ == "__main__":
    main()
