def solution():
    def integers():
        i = 1
        while True:
            yield i

            i += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(end, seq):
        result = []
        for n, i in enumerate(seq):
            if n < end:
                result.append(i)
            else:
                break

        return result
    
    return (take, halves, integers)

take = solution()[0]

halves = solution()[1]

print(take(5, halves()))