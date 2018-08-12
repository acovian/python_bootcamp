def cached_execution(cache, proc, proc_input):
    if proc_input not in cache:
        cache[proc_input] = proc(proc_input)
    return cache[proc_input]

def cached_fibo(n):
    assert n > -1
    if n == 0 or n == 1:
        return n
    else:
        return cached_execution(cache, cached_fibo, n-1) + \
            cached_execution(cache, cached_fibo, n-2)

def main():
    while True:
        print(cached_fibo(int(input('Which Fibonacci number do you want: '))))

if __name__ == '__main__':
    cache = {}
    main()
