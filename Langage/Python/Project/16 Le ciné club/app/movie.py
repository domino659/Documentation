import os, json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    with open(DATA_FILE, "r") as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    # movies = []
    # for movie_title in movies_title:
    #     movies.append(Movie(movie_title))
    return movies

class Movie:
    def __init__(self, title):
        self.title = title.title()
    
    def __str__(self):
        return f"{self.title}"

    def _get_movie(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)
            return True

    def add_to_movies(self):
        movies = self._get_movie()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà enregistré.")
            return False

    def remove_from_movies(self):
        movies = self._get_movie()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'existe pas.")
            return False

if __name__ == "__main__":
    # movie = Movie("Guerre des chatons")
    # movie.add_to_movies()
    # movie.remove_from_movies()
    movies = get_movies()
    print(movies)
