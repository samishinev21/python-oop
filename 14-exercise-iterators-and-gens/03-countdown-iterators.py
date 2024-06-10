class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = self.count

    def __iter__(self):
        return self

    def __next__(self):
        i = self.i
        self.i -= 1

        if i <= self.count and i >= 0:
            return i
        else:
            raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")