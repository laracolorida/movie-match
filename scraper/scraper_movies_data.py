from time import sleep
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup

users_ratings = pd.read_csv('users_ratings.csv', encoding='utf-8')
movies_links = users_ratings['movie_link'].unique()


def split_url_and_get_value(url):
    split_items = url.split("/")
    return split_items[-2]


def scraper_movie_data(movie):
    response = requests.get(movie)

    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        imdb = soup.find(attrs={"data-track-action": "IMDb"})
        imdb = imdb.attrs["href"]

        tmdb = soup.find(attrs={"data-track-action": "TMDb"})
        tmdb = tmdb.attrs["href"]

        imdb = split_url_and_get_value(imdb)
        imdb = imdb.replace('t', "")

        tmdb = split_url_and_get_value(tmdb)
        movie_name = split_url_and_get_value(movie)
        
        a_tags = soup.find_all("a")

        href_values = [a.get("href") for a in a_tags]

        genres = []

        for href in href_values:
            if href and "/films/genre/" in href:
                genres.append(split_url_and_get_value(href))
        
        genres = "|".join(genres)
        
        
        movie_data = users_ratings[users_ratings["movie_link"] == movie]
        movie_data = movie_data["movie_title"].unique()[0]

        print([movie_name, imdb, tmdb, genres, movie_data])

        return [movie_name, imdb, tmdb, genres, movie_data]


def iterate_over_movies():
    movies_data = []

    for movie in movies_links:
        movies_data.append(scraper_movie_data(movie))
        
    return movies_data


movies_data = iterate_over_movies()

header = ['letterbox', 'imdbId', 'tmdbId', 'genres', 'title']

with open("custom_movies.csv", 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(header)

    for movie in movies_data:
        writer.writerow(movie)
