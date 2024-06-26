def vowel_filter(function):
    def wrapper():
        letters = function()
        result = []

        for letter in letters:
            if letter in "aeoui":
                result.append(letter)

        return result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())