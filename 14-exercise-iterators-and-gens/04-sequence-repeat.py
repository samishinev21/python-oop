class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0
        self.times = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        i = self.i

        if self.i < len(self.sequence) - 1:
            self.i += 1
        else:
            self.i = 0

        self.times += 1

        if self.times > self.number:
            raise StopIteration
        else:
            return self.sequence[i]
        
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')