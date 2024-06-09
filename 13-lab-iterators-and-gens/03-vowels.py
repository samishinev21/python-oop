class vowels:
    def __init__(self, word):
        self.vowels = [v for v in word if v.lower() in ["a", "e", "i", "u", "y", "o"]]
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        i = self.i
        self.i += 1

        if i <= len(self.vowels) - 1:
            return self.vowels[i]
        else:
            raise StopIteration
        
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)