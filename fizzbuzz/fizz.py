def fizz(n):
    fb = ''

    if n % 3 == 0:
        fb += "fizz"
    if n % 5 == 0:
        fb += "buzz"
    if n % 3 != 0 and n % 5 != 0:
        fb = n
        
    return fb


if __name__ == '__main__':
    for n in range(1, 20):
        print(fizz(n))