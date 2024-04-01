class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)
                self.guests += people
                break
    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()
                break

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\nFree rooms: "
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result += f"{', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
        return result
