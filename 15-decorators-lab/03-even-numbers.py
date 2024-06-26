def even_numbers(function):
    def wrapper(numbers):
        all_nums = function(numbers)
        result = []

        for number in all_nums:
            if number % 2 == 0:
                result.append(number)

        return result
         
    return wrapper

@even_numbers

def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))