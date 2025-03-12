import requests

# метод запроса к API
def send_request(genre: str):
    url = 'https://kinopoiskapiunofficial.tech/api/v2.2/films'

    genres_id = {'action' : 1,
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
                 'war' : 11
                 }

    headers = {
        'accept' : 'application/json',
        'X-API-KEY' : '9b2a9299-053f-488e-863f-68dbadc18ecf'
    }

    params = {
        'genres' : [3],
        'notNullFields' : ['nameRu', 'nameOriginal', 'posterUrl', 'year', 'ratingKinopoisk', 'ratingImdb', 'description'],
        'selectFields' : ['poster', 'name', 'type', 'year', 'rating', 'genres', 'id', 'description']
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    films_api = response.json()
    return films_api['items']

# форматирование ответа
def format_data(data: dict):
    formatted_data = []
    for film in data:
        nameRu = film['nameRu']
        nameOriginal = film['nameOriginal']
        year = film['year']
        ratingKinopoisk = film['ratingKinopoisk']
        ratingImdb = film['ratingImdb']
        id = film['kinopoiskId']
        genres = ", ".join(g["genre"] for g in film["genres"])
        url_poster = film['posterUrl']
        if 'description' in film.keys():
            film_description = film['description']
        else:
            film_description = '-'
        if 'ratingAgeLimits' in film.keys():
            age_limits = film['ratingAgeLimits']
        else:
            age_limits = ''
        country = ', '.join(c['country'] for c in film['countries'])

        formatted_data.append(
            f'''{url_poster}
            \n{nameRu}/{nameOriginal} ({year})     {ratingKinopoisk}(Imdb - {ratingImdb})
            \nЖанр: {genres}     {age_limits}
            \nСтрана: {country}
            \nОписание: {film_description}
            \nId: {id}'''
        )
    return formatted_data