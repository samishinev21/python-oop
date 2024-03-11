class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self ,song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return f"Cannot add songs. Album is published."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        
    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        songs = []
        found = False

        for song in self.songs:
            if song.name == song_name:
                found = True
            else:
                songs.append(song)

        self.songs = songs
        if found:
            return f"Removed song {song_name} from album {self.name}."
        else:
            return f"Song is not in the album."
        
    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        songs = []

        for song in self.songs:
            songs.append(song.get_info())

        songs_info = "\n".join(songs)

        return f"Album {self.name}\n{songs_info}"
        