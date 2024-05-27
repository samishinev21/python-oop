class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        
        self.i = len(self.iterable) - 1
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= self.n:
            i = self.i
            self.i -= 1
            return self.iterable[i]
        else:
            raise StopIteration