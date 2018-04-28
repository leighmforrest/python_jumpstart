def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print("5!={:,}, 3!={:,}, 11!={:,}".format(factorial(5), factorial(3), factorial(11)))