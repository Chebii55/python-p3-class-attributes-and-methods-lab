# song.py
class Song:
    artists = []
    count = 0
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_songs()
        Song.add_artist_to_artists(artist)
        Song.add_genre_to_genres(genre)
        Song.update_genre_count(genre)
        Song.update_artist_count(artist)

    @classmethod
    def add_song_to_songs(cls):
        cls.count += 1

    @classmethod
    def add_artist_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_genre_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def update_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def update_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
