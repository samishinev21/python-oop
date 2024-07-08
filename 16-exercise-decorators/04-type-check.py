def type_check(the_type):
    def decorator(function):
        def wrapper(param):
            if type(param) == the_type:
                return function(param)
            else:
                return "Bad Type"
            
        return wrapper
    
    return decorator

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))