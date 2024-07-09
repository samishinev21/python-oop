def tags(sign):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f"<{sign}>{''.join(result)}</{sign}>"

        return wrapper
    
    return decorator

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))