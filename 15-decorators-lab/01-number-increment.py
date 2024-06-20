def number_increment(numbers):
    def increase():
        result = []
        for number in numbers:
            result.append(number + 1)

        return result

    return increase()

print(number_increment([1, 2, 3]))