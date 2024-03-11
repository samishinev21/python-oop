class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}"
    
    def remove_album(self, album_name):
        albums = []
        album_to_remove = False

        for album in self.albums:
            if album.name == album_name:
                album_to_remove = album
            else:
                albums.append(album)

        if album_to_remove and not album_to_remove.published:
            self.albums = albums
            return f"Album {album_name} has been removed."
        elif album_to_remove and album_to_remove.published:
            return f"Album has been published. It cannot be removed."
        else:
            return f"Album {album_name} is not found."
        
    def details(self):
        albums = []

        for album in self.albums:
            albums.append(album.details())

        info = "\n".join(albums)

        return f"Band {self.name}\n{info}"