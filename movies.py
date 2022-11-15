import json
import webbrowser
from tkinter.messagebox import NO
from turtle import title
from genres import genres
from pprint import pprint
from time import sleep


class Movies:

    # class constructor
    def __init__(self):
        # print('# init called')

        self.titles = []
        self.movie_links = []
        self.description = []

        self.genres = [item.lower() for item in genres]
        # print(self.genres)

    def __enter__(self):
        print('# enter called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('# exit called')

    def read_movies_file(self):
        with open('movies.json') as json_file:
            movies = json.load(json_file)

        #print("    - Data-Type: ", type(movies))
        # pprint(movies)
        return movies

    def choose_genre(self):
        print('Choose a genre from the list of genres below:')
        for item in self.genres:
            print(item)

        user_choice = None
        while user_choice not in self.genres:
            user_choice = input('Type your choice here: ').lower()
            if user_choice not in self.genres:
                print('Invalid genre name. Please enter a valid name\n')

        return user_choice

    def get_movie_info(self, user_choice, movies):
        if user_choice in self.genres:
            for m in movies:
                if movies[m]['genre'].lower() == user_choice:

                    title = movies[m]['title']
                    description = movies[m]['description']
                    url = movies[m]['movie link']
                    self.titles.append(title)
                    self.description.append(description)
                    self.movie_links.append(url)

            zipped_movies = zip(
                self.titles, self.description, self.movie_links)
            movie_info = list(zipped_movies)
            print('Great choice!')
            print('here is a list of', len(self.titles),
                  user_choice, 'movies for your viewing pleasure:')
            for m in self.titles:
                print('-', m)

        return movie_info

    def get_movie(self, movie_info):
        matched = False
        while matched == False:
            movie_choice = input(
                'which movie would you love to watch? ').lower()
            for index, item in enumerate(movie_info):
                if movie_info[index][0].lower() == movie_choice:
                    matched = True
                    print('\n')
                    print('About the movie: {}'.format(movie_choice))
                    words = movie_info[index][1].split(' ')
                    for word in words:
                        print(word, end=' ', flush=True)
                        sleep(0.5)
                    print('\n')
                    message = input(
                        'Do you want to watch the movie trailer? Yes(y) / No(n) ').lower()
                    if message == 'yes' or message == 'y':
                        webbrowser.open(movie_info[index][2])
                    else:
                        print('Thank you for your time.')
