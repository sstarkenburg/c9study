def fib(n):
    if n <= 1:
       return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    for n in range(1, 10):
        print(fib(n))