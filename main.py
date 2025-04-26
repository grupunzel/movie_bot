import telebot
from telebot import types
import random
from hooks import send_request, format_data, random_film, new_films, best_of_the_best, add_to_wishlist, remove_from_wishlist, print_wishlist, film_description

API_TOKEN = 'BOT_API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)
bot.set_webhook()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    new_film = types.KeyboardButton('Новинки \U0001F31F')
    recommend_film = types.KeyboardButton('Рекомендации фильмов \U0001F378')
    best_films = types.KeyboardButton('Лучшие из лучших \U0001F525')
    film_random = types.KeyboardButton('Рандомный фильм \U0001F3AC')
    wishlist = types.KeyboardButton('Посмотреть Избранное \U0001F4CD')
    markup.add(new_film, recommend_film, best_films, film_random, wishlist)
    bot.send_message(message.chat.id, "Привет! \U0001F44B Я твой MovieBot, нажми на любую кнопку в меню, и я помогу тебе выбрать, что посмотреть.", reply_markup=markup)

global results_list
results_list = []
genres_en = ['action', 'adventure', 'comedy', 'crime', 'drama', 'fantasy', 'history', 'horror', 'musical', 'mistery', 'romance', 'sci_fi', 'war']
genres_ru = ['боевик', 'приключения', 'комедия', 'криминал', 'драма', 'фэнтези', 'история', 'ужасы', 'мюзикл', 'детектив', 'мелодрама', 'фантастика', 'военный']

@bot.callback_query_handler(func=lambda c:True)
def ans(c):
    cid = c.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    again = types.InlineKeyboardButton(text='Повторить', callback_data='again')
    result = []

    for genre in genres_en:
        if c.data == f'{genre}_rec':
            genre_ru = genres_ru[genres_en.index(genre)]
            result = format_data(send_request(genre_ru))
            results_list.append(result[1])
            again = types.InlineKeyboardButton(text='Повторить', callback_data=f'{genre}_rec')
            bot.send_message(cid, f"{genre_ru.capitalize()}:")

        elif c.data == f'{genre}_ran':
            genre_ru = genres_ru[genres_en.index(genre)]
            result = format_data(random_film(genre_ru))
            results_list.append(result[1])
            again = types.InlineKeyboardButton(text='Повторить', callback_data=f'{genre}_ran')
            bot.send_message(cid, f"Случайный фильм в жанре {genre_ru}:")

    if c.data == 'random_f_rec':
        genre = genres_ru[random.randint(0, 12)]
        result = format_data(send_request(genre))
        results_list.append(result[1])
        again = types.InlineKeyboardButton(text='Повторить', callback_data='random_f_rec')
        bot.send_message(cid, f"Случайные рекомендации в жанре {genre}:") 
    elif c.data == 'random_f_ran':
        genre = genres_ru[random.randint(0, 12)]
        result = format_data(random_film(genre))
        results_list.append(result[1])
        again = types.InlineKeyboardButton(text='Повторить', callback_data='random_f_ran')
        bot.send_message(cid, f"Случайный фильм в жанре {genre}:")
    elif c.data == "back":
        msg = bot.send_message(cid, 'Вы на Главном Меню.')
        bot.register_next_step_handler(msg, send_welcome)
    elif c.data == 'new_films':
        result = send_new_films(cid)
    elif c.data == 'best_films':
        result = send_best_films(cid)
    wishlist_list = print_wishlist()
    keyboard.add(back, again)
    if len(result) != 0 and result[0] != 'Ф':
        i = 0
        index_result = results_list.index(result[1])
        for elem in result[0]:
            keyboard_wishlist = types.InlineKeyboardMarkup()
            add_wishlist = types.InlineKeyboardButton(text='Добавить в Избранное \U0001F4CD', callback_data=f'add_film_{i}_{index_result}')
            keyboard_wishlist.add(add_wishlist)
            bot.send_message(cid, ''.join(elem), reply_markup=keyboard_wishlist, parse_mode='HTML')
            i += 1
        bot.send_message(cid, 'Предложить еще фильмы?', reply_markup=keyboard)
    for i in range(len(wishlist_list)):
        if c.data == f'remove_film_{i}':
            result = remove_from_wishlist(i)
            bot.delete_message(chat_id=cid, message_id=c.message.message_id)
    for i in range(0, 5):
        for index in range(len(results_list)):
            if c.data == f'add_film_{i}_{index}':
                id_list = results_list[index]
                result = add_to_wishlist(id_list[i])
                if not isinstance(result, str):
                    bot.edit_message_text(
                        chat_id=cid,
                        message_id=c.message.message_id,
                        text=format_data([film_description(id_list[i])])[0][0] + '\n\n\nФильм добавлен в Избранное\U0001F4CD\n\n',
                        parse_mode='HTML'
                    )
                else:
                    bot.edit_message_text(
                        chat_id=cid,
                        message_id=c.message.message_id,
                        text=format_data([film_description(id_list[i])])[0][0] + f'\n\n\nФильм уже добавлен в Избранное \U0001F4CD\n\n',
                        parse_mode='HTML'
                    )


def send_new_films(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    again = types.InlineKeyboardButton(text='Повторить', callback_data='new_films')
    bot.send_message(chat_id, 'Новинки фильмов: ')
    keyboard.add(back, again)
    result = format_data(new_films())
    results_list.append(result[1])
    i = 0
    for elem in result[0]:
        keyboard_wishlist = types.InlineKeyboardMarkup()
        add_wishlist = types.InlineKeyboardButton(text='Добавить в Избранное \U0001F4CD', callback_data=f'add_film_{i}')
        keyboard_wishlist.add(add_wishlist)
        bot.send_message(chat_id, ''.join(elem), reply_markup=keyboard_wishlist, parse_mode='HTML')
        i += 1
    bot.send_message(chat_id, 'Предложить еще фильмы?', reply_markup=keyboard)
    return result


def send_best_films(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    again = types.InlineKeyboardButton(text='Повторить', callback_data='best_films')
    bot.send_message(chat_id, "Лучшие фильмы: ")
    keyboard.add(back, again)
    result = format_data(best_of_the_best())
    results_list.append(result[1])
    i = 0
    for elem in result[0]:
        keyboard_wishlist = types.InlineKeyboardMarkup()
        add_wishlist = types.InlineKeyboardButton(text='Добавить в Избранное \U0001F4CD', callback_data=f'add_film_{i}')
        keyboard_wishlist.add(add_wishlist)
        bot.send_message(chat_id, ''.join(elem), reply_markup=keyboard_wishlist, parse_mode='HTML')
        i += 1
    bot.send_message(chat_id, 'Предложить еще фильмы?', reply_markup=keyboard)
    return result


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'Новинки \U0001F31F':
        send_new_films(message.chat.id)

    elif message.text == 'Рекомендации фильмов \U0001F378':
        action = types.InlineKeyboardButton(text='Боевик \U0001F4A5', callback_data='action_rec')
        adventure = types.InlineKeyboardButton(text='Приключения \U0001F9D7', callback_data='adventure_rec')
        comedy = types.InlineKeyboardButton(text='Комедия \U0001F639', callback_data='comedy_rec')
        crime = types.InlineKeyboardButton(text='Криминал \U0001FA78', callback_data='crime_rec')
        drama = types.InlineKeyboardButton(text='Драма \U0001F3AD', callback_data='drama_rec')
        fantasy = types.InlineKeyboardButton(text='Фэнтези \U0001F9DD', callback_data='fantasy_rec')
        history = types.InlineKeyboardButton(text='История \U0001F5E1', callback_data='history_rec')
        horror = types.InlineKeyboardButton(text='Ужасы \U0001F9DF', callback_data='horror_rec')
        musical = types.InlineKeyboardButton(text='Мюзикл \U0001F3B6', callback_data='musical_rec')
        mistery = types.InlineKeyboardButton(text='Детектив \U0001F50E', callback_data='mistery_rec')
        romance = types.InlineKeyboardButton(text='Мелодрама \U0001F48F', callback_data='romance_rec')
        sci_fi = types.InlineKeyboardButton(text='Фантастика \U0001F47D', callback_data='sci_fi_rec')
        war = types.InlineKeyboardButton(text='Военный \U0001F93C', callback_data='war_rec')
        random_f = types.InlineKeyboardButton(text='Случайный \U0001F440', callback_data='random_f_rec')
        back = types.InlineKeyboardButton(text='Назад в меню', callback_data='back')
        keyboard = [
            [action, adventure, comedy],
            [crime, drama, fantasy],
            [history, horror, musical],
            [mistery, romance, sci_fi],
            [war, random_f],
            [back]
        ]
        markup_genre = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup_genre)

    elif message.text == 'Лучшие из лучших \U0001F525':
        send_best_films(message.chat.id)

    elif message.text == 'Рандомный фильм \U0001F3AC':
        action = types.InlineKeyboardButton(text='Боевик \U0001F4A5', callback_data='action_ran')
        adventure = types.InlineKeyboardButton(text='Приключения \U0001F9D7', callback_data='adventure_ran')
        comedy = types.InlineKeyboardButton(text='Комедия \U0001F639', callback_data='comedy_ran')
        crime = types.InlineKeyboardButton(text='Криминал \U0001FA78', callback_data='crime_ran')
        drama = types.InlineKeyboardButton(text='Драма \U0001F3AD', callback_data='drama_ran')
        fantasy = types.InlineKeyboardButton(text='Фэнтези \U0001F9DD', callback_data='fantasy_ran')
        history = types.InlineKeyboardButton(text='История \U0001F5E1', callback_data='history_ran')
        horror = types.InlineKeyboardButton(text='Ужасы \U0001F9DF', callback_data='horror_ran')
        musical = types.InlineKeyboardButton(text='Мюзикл \U0001F3B6', callback_data='musical_ran')
        mistery = types.InlineKeyboardButton(text='Детектив \U0001F50E', callback_data='mistery_ran')
        romance = types.InlineKeyboardButton(text='Мелодрама \U0001F48F', callback_data='romance_ran')
        sci_fi = types.InlineKeyboardButton(text='Фантастика \U0001F47D', callback_data='sci_fi_ran')
        war = types.InlineKeyboardButton(text='Военный \U0001F93C', callback_data='war_ran')
        random_f = types.InlineKeyboardButton(text='Случайный \U0001F440', callback_data='random_f_ran')
        back = types.InlineKeyboardButton(text='Назад в меню', callback_data='back')
        keyboard = [
            [action, adventure, comedy],
            [crime, drama, fantasy],
            [history, horror, musical],
            [mistery, romance, sci_fi],
            [war, random_f],
            [back]
        ]
        markup_genre = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup_genre)

    elif message.text == 'Посмотреть Избранное \U0001F4CD':
        result = print_wishlist()
        i = 0
        bot.send_message(message.chat.id, f"В Избранном {len(result) - result.count('')} фильмов.")
        if len(result) == 0:
            bot.send_message(message.chat.id, 'Тут пусто :(')
        for elem in result:
            if elem != '':
                keyboard_wishlist = types.InlineKeyboardMarkup()
                remove_wishlist = types.InlineKeyboardButton(text='Удалить из Избранного \U0001F4CD', callback_data=f'remove_film_{i}')
                keyboard_wishlist.add(remove_wishlist)
                bot.send_message(message.chat.id, elem, reply_markup=keyboard_wishlist, parse_mode='HTML')
            i += 1
    
    else:
        bot.send_message(message.chat.id, 'Извините, но у меня нет такой функции :( Чтобы продолжить, нажмите на любую кнопку из предложенных.')

bot.infinity_polling()
