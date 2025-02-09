import requests
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv("THEMOVIEDB_API_KEY")}"
    }


def get_top_movies(page):
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page="+str(page)
    response = requests.get(url, headers=headers)

    if not response.ok:
        raise ConnectionError()

    return response.json()['results']

def get_movie_by_id(id):
    url = "https://api.themoviedb.org/3/movie/"+str(id)+"?language=en-US"
    response = requests.get(url, headers=headers)

    if not response.ok:
        raise ConnectionError()
    
    return response.json()


if __name__=="__main__":
    print(type(get_top_movies(1)[0]))
