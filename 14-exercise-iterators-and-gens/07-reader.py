def read_next(*args):
    tokens = []

    for token in args:
        for char in token:
            tokens.append(char)

    for char in tokens:
        yield char

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')