class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0
        self.returned_nums = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        number = self.number
        self.returned_nums += 1
        self.number += self.step


        if self.returned_nums <= self.count:
            return number
        else:
            raise StopIteration
        
numbers = take_skip(2, 6)
for number in numbers:
    print(number)