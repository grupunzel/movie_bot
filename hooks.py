import requests
import random

# метод запроса к API
def send_request(genre: str):
    url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=FILM&ratingFrom=0&ratingTo=10&yearFrom=1000&yearTo=3000&page=1'

    genres_id = {'action' : 11,
                 'adventure' : 7,
                 'comedy' : 13,
                 'crime' : 3,
                 'drama' : 2,
                 'fantasy' : 12,
                 'history' : 15,
                 'horror' : 17,
                 'musical' : 20,
                 'mistery' : 5,
                 'romance' : 4,
                 'sci-fi' : 6,
                 'war' : 14,
                 }

    headers = {
        'accept' : 'application/json',
        'X-API-KEY' : '9b2a9299-053f-488e-863f-68dbadc18ecf'
    }

    params = {
        'genres' : [genres_id[genre]],
        'type' : 'FILM',
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    films_api = response.json()
    return films_api['items']


#получение от апи описание фильма
def film_description(id):
    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}'

    headers = {
        'accept': 'application/json',
        'X-API-KEY': '9b2a9299-053f-488e-863f-68dbadc18ecf'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    films_description = response.json()
    return films_description


#получение трейлера фильма
def film_trailer(id):
    url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{id}/videos'

    headers = {
        'accept': 'application/json',
        'X-API-KEY': '9b2a9299-053f-488e-863f-68dbadc18ecf'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    film_trailers = response.json()
    return film_trailers['items']



#рандомный фильм
def random_film(genre):
    film = send_request(genre)
    return film[random.randint(0, len(film))]

# форматирование ответа
def format_data(data: dict, genre: str):
    formatted_data = []
    print(type(data))
    for film in data:
        nameRu = film['nameRu']
        nameOriginal = film['nameOriginal']
        year = film['year']
        ratingKinopoisk = film['ratingKinopoisk']
        ratingImdb = film['ratingImdb']
        id = film['kinopoiskId']
        countries = ", ".join(g["country"] for g in film["countries"])
        genres = ", ".join(g["genre"] for g in film["genres"])
        url_poster = film['posterUrl']

        Description = film_description(id)
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

        if film['genres'][0]['genre'] == genre:
            formatted_data.append(
                f'''{url_poster}
                \n{nameRu}/{nameOriginal} ({year})     {ratingKinopoisk}(Imdb - {ratingImdb})
                \nЖанр: {genres}     
                \nСтрана: {countries}
                \nОписание: {description}
                \nId: {id}
                \nТрейлер: {trailer}'''
            )
    formatted_data5 = []
    i = 0
    while i < 5:
        film = formatted_data[random.randint(0, len(formatted_data) - 1)]
        if not film in formatted_data5:
            formatted_data5.append(film)
            i += 1

    return formatted_data5
