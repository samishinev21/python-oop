def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        previous = a
        a = a + b
        b = previous

generator = fibonacci()
for i in range(10):
    print(next(generator))