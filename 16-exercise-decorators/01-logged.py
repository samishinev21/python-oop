def logged(function):
    def wrapper(*params):
        result = function(*params)
        return f"you called {function.__name__}{params}\nit returned {result}"
    
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))