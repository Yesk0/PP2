# 1
def square(n):
    for i in range(1, n + 1):
        yield i ** 2


squares = square(5)
print(next(squares))
print(next(squares))
print(next(squares))


# 2

def evens_in_range(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


numbers = evens_in_range(10)
print(*numbers, sep=", ")


# 3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print(*divisible_by_3_and_4(30), sep=", ")


# 4
def squares_between_range(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2


print(*squares_between_range(10, 20))


# 5

def reduce(n):
    for i in range(0, n):
        yield n - i


print(*reduce(10), sep=", ")