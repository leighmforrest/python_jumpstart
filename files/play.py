def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums

def fibonacci_co():
    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current


if __name__ == '__main__':
    # print("5!={:,}, 3!={:,}, 11!={:,}".format(factorial(5), factorial(3), factorial(11)))
    for i in fibonacci_co():
        if i > 1000:
            break

        print(i)