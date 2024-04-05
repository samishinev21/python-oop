import math

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.current_row = 0
        self.current_col = 0
        self.max_row = self.pages - 1
        self.max_col = PhotoAlbum.PHOTOS_PER_PAGE

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(math.ceil(photos_count/cls.PHOTOS_PER_PAGE))

    def add_photo(self, label):
        if self.current_col == self.max_col and self.current_row == self.max_row:
            return "No more free slots"
        elif self.current_col == self.max_col:
            self.current_col = 0
            self.current_row += 1
            self.photos[self.current_row].append(label)
        else:
            self.current_col += 1
            self.photos[self.current_row].append(label)
        return f"{label} phot added successfully on page {self.current_row + 1} slot {self.current_col + 1}"

    def display(self):
        result = "-----------\n"
        for row in range(0, self.pages):
            result += " ".join(["[]" for _ in self.photos[row]])
            result += "\n-----------\n"
        
        return result

import unittest

class TestsPhotoAlbum(unittest.TestCase):
    def test_init_creates_all_attributes(self):
        album = PhotoAlbum(2)
        self.assertEqual(album.pages, 2)
        self.assertEqual(album.photos, [[], []])

    def test_from_photos_should_create_instace(self):
        album = PhotoAlbum.from_photos_count(12)
        self.assertEqual(album.pages, 3)
        self.assertEqual(album.photos, [[], [], []])
        
    def test_add_photo_with_no_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.add_photo("prom")
        self.assertEqual(result, "No more free slots")
        
    def test_add_photo_with_free_spots(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        self.assertEqual(album.photos, [['baby', 'first grade', 'eight grade', 'party with friends']])
        
    def test_display_with_one_page(self):
        album = PhotoAlbum(1)
        album.add_photo("baby")
        album.add_photo("first grade")
        album.add_photo("eight grade")
        album.add_photo("party with friends")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------")
        
    def test_display_with_three_pages(self):
        album = PhotoAlbum(3)
        for _ in range(8):
            album.add_photo("asdf")
        result = album.display().strip()
        self.assertEqual(result, "-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------")
        

if __name__ == "__main__":
    unittest.main()