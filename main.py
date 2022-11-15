from movies import Movies


def main():
    movie = Movies()
    movies = movie.read_movies_file()
    selected_genre = movie.choose_genre()
    movie_info = movie.get_movie_info(selected_genre, movies)
    movie.get_movie(movie_info)


if __name__ == '__main__':
    main()
