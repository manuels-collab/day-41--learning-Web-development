import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

movie_response = requests.get(URL)
soup = BeautifulSoup(movie_response.text, 'html.parser')
movie_content = soup.find_all(name='h3', class_="title")
movies = [movie.getText() for movie in reversed(movie_content)]
print(movies)
for item in movies:
    with open("movie_file", "a", encoding="utf-8") as file:
        file.write(f"{item}")
        file.write(f"\n")
# Write your code below this line: 👇


