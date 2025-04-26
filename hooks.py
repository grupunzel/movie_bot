import requests
import random

# метод запроса к API
def send_request(genre: str):
    url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=FILM&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&page=1'

    genres_id = {'боевик' : 11,
                 'приключения' : 7,
                 'комедия' : 13,
                 'криминал' : 3,
                 'драма' : 2,
                 'фэнтези' : 12,
                 'история' : 15,
                 'ужасы' : 17,
                 'мюзикл' : 20,
                 'детектив' : 5,
                 'мелодрама' : 4,
                 'фантастика' : 6,
                 'военный' : 14,
                 }

    headers = {
        'accept' : 'application/json',
        'X-API-KEY' : 'API_KEY'
    }

    params = {
        'genres' : [genres_id[genre]],
        'type' : 'FILM',
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    films_api = response.json()
    films = films_api['items']
    for film in films:
        if film['genres'][0]['genre'] != genre:
            films.remove(film)
    for film in films:
        for g in film['genres']:
            if g['genre'] == 'мультфильм' or g['genre'] == 'детский':
                films.remove(film)
                break
    return films


#получение от апи описание фильма
def film_description(id):
    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}'

    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'API_KEY'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    films_description = response.json()
    return films_description


def get_film_poster(id):
    result = film_description(id)
    return result['posterUrl']


#получение трейлера фильма
def film_trailer(id):
    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}/videos'

    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'API_KEY'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    film_trailers = response.json()
    return film_trailers['items']



#рандомный фильм
def random_film(genre):
    films_list = send_request(genre)
    answer = films_list[random.randint(0, len(films_list) - 1)]
    return [answer]


#новые фильмы
def new_films():
    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres?year=2025&month=JANUARY'

    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'API_KEY'
    }

    params = {
        'year': 2025,
    }

    response_january = requests.get(url, params=params, headers=headers)
    if response_january.status_code != 200:
        return None
    new_film_january = response_january.json()
    new_films_january = new_film_january['items']

    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres?year=2025&month=FEBRUARY'

    response_february = requests.get(url, params=params, headers=headers)
    if response_february.status_code != 200:
        return None
    new_film_february = response_february.json()
    new_films_february = new_film_february['items']

    new_films_list = new_films_january + new_films_february

    new_films_list5 = []
    i = 0
    while i < 5:
        new_film = new_films_list[random.randint(0, len(new_films_list) - 1)]
        if not new_film in new_films_list5 and (new_film['year'] == 2025 or  new_film['year'] == 2024) and new_film['genres'][0]['genre'] != 'мультфильм' and new_film['genres'][0]['genre'] != 'детский':
            new_films_list5.append(new_film)
            i += 1
    for i in range(len(new_films_list5)):
        film = new_films_list5[i]
        new_films_list5[i] = film_description(film['kinopoiskId'])

    return new_films_list5


#лучшие из лучших фильмы
def best_of_the_best():
    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/collections?type=TOP_250_MOVIES&page=1'

    headers = {
        'accept': 'application/json',
        'X-API-KEY': 'API_KEY'
    }

    params = {
        'type': 'FILM',
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    response_json = response.json()
    best_films = response_json['items']
    best_films5 = []
    i = 0
    while i < 5:
        film = best_films[random.randint(0, len(best_films) - 1)]
        if not film in best_films5:
            best_films5.append(film)
            i += 1

    return best_films5

global wishlist
wishlist = []
global wishlist_id
wishlist_id = []

def add_to_wishlist(id):
    data = format_data([film_description(id)])[0]
    if not data in wishlist:
        wishlist.append(data)
        wishlist_id.append(id)
        return wishlist
    else:
        return 'Фильм уже добавлен в Избранное \U0001F4CD'

def print_wishlist():
    return wishlist

def remove_from_wishlist(id):
    wishlist[id] = ''
    return 'Фильм удален из Избранного.'


# форматирование ответа
def format_data(data: list):
    formatted_data = []
    id_list = []
    for film in data:
        id = film['kinopoiskId']
        Description = film_description(id)
        nameRu = Description['nameRu']
        nameOriginal = Description['nameOriginal']
        year = Description['year']
        ratingKinopoisk = Description['ratingKinopoisk']
        ratingImdb = Description['ratingImdb']
        countries = ", ".join(g["country"] for g in Description["countries"])
        genres = ", ".join(g["genre"] for g in Description["genres"])
        url_poster = Description['posterUrl']

        if not Description['description'] == None:
            description = Description['description']
        elif not Description['shortDescription'] == None:
            description = Description['shortDescription']
        else:
            description = '-'

        Trailers = film_trailer(id)
        if len(Trailers) != 0:
            trailer = Trailers[0]['url']
        else:
            trailer = ''

        formatted_data.append(
            f'''<b>{nameRu}/{nameOriginal}</b>   ({year})
            \n{ratingKinopoisk}(IMDb - {ratingImdb})
            \n<b>Жанр</b>: {genres}     
            \n<b>Страна</b>: {countries}
            \n<b>Описание</b>: {description}
            \n<b>Id</b><a href='{url_poster}'>: </a>{id}
            \n<b>Трейлер</b>: {trailer}'''
        )
        id_list.append(id)
    if len(formatted_data) > 1 :
        formatted_data5 = []
        id_list_5 = []
        i = 0
        while i < 5:
            random_index = random.randint(0, len(formatted_data) - 1)
            film = formatted_data[random_index]
            if not film in formatted_data5:
                formatted_data5.append(film)
                id_list_5.append(id_list[random_index])
                i += 1
        return [formatted_data5, id_list_5]
    else:
        return [formatted_data, id_list]
