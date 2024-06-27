def even_parameters(function):
    def wrapper(*nums):
        result = None
        for num in nums:
            if type(num) != int or num % 2 != 0:
                result = "Please use only even numbers!"
                break

        else:
            result = function(*nums)

        return result
    
    return wrapper

@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))