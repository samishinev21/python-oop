class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = [(key, value) for (key, value) in dictionary.items()]
        self.i = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        i = self.i
        self.i += 1

        if i <= len(self.dictionary) - 1:
            return self.dictionary[i]
        else:
            raise StopIteration
        
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)