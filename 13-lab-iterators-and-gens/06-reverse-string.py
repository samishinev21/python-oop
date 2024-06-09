def reverse_text(word):
    for i in range(len(word) - 1, -1, -1):
        yield word[i]

for char in reverse_text("step"):
    print(char, end='')