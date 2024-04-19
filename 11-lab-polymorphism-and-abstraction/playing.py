def start_playing(object):
    return object.play()

class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))