import telebot
from telebot import types
from hooks import send_request, format_data, random_film, new_films, best_of_the_best, add_to_wishlist, remove_from_wishlist, wishlist, print_id_list

API_TOKEN = '7818305458:AAHql1NDOblTnOy48LjLDhue-mrjWc2PsDQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    new_film = types.KeyboardButton('Новинки \U0001F31F')
    recommend_film = types.KeyboardButton('Рекомендации фильмов \U0001F378')
    best_films = types.KeyboardButton('Лучшие из лучших \U0001F525')
    film_random = types.KeyboardButton('Рандомный фильм \U0001F3AC')
    wishlist = types.KeyboardButton('Посмотреть Избранное \U0001F4CD')
    markup.add(new_film, recommend_film, best_films, film_random, wishlist)
    bot.send_message(message.chat.id, "Привет! Я твой MovieBot, нажми на любую кнопку в меню, и я помогу тебе выбрать, что посмотреть.", reply_markup=markup)


@bot.callback_query_handler(func=lambda c:True)
def ans(c):
    cid = c.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    again = types.InlineKeyboardButton(text='Повторить', callback_data='back')
    result = []
    if c.data == "action_rec":
        result = format_data(send_request('боевик'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='action_rec')
    elif c.data == "adventure_rec":
        result = format_data(send_request('приключения'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='adventure_rec')
    elif c.data == "comedy_rec":
        result = format_data(send_request('комедия'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='comedy_rec')
    elif c.data == "crime_rec":
        result = format_data(send_request('криминал'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='crime_rec')
    elif c.data == "drama_rec":
        result = format_data(send_request('драма'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='drama_rec')
    elif c.data == "fantasy_rec":
        result = format_data(send_request('фэнтези'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='fantasy_rec')
    elif c.data == "history_rec":
        result = format_data(send_request('история'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='history_rec')
    elif c.data == "horror_rec":
        result = format_data(send_request('ужасы'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='horror_rec')
    elif c.data == "musical_rec":
        result = format_data(send_request('мюзикл'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='musical_rec')
    elif c.data == "mistery_rec":
        result = format_data(send_request('детектив'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='mistery_rec')
    elif c.data == "romance_rec":
        result = format_data(send_request('мелодрама'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='romance_rec')
    elif c.data == "sci_fi_rec":
        result = format_data(send_request('фантастика'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='sci_fi_rec')
    elif c.data == "war_rec":
        result = format_data(send_request('военный'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='war_rec')

    elif c.data == "action_ran":
        result = format_data(random_film('боевик'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='action_ran')
    elif c.data == "adventure_ran":
        result = format_data(random_film('приключения'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='adventure_ran')
    elif c.data == "comedy_ran":
        result = format_data(random_film('комедия'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='comedy_ran')
    elif c.data == "crime_ran":
        result = format_data(random_film('криминал'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='crime_ran')
    elif c.data == "drama_ran":
        result = format_data(random_film('драма'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='drama_ran')
    elif c.data == "fantasy_ran":
        result = format_data(random_film('фэнтези'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='fantasy_ran')
    elif c.data == "history_ran":
        result = format_data(random_film('история'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='history_ran')
    elif c.data == "horror_ran":
        result = format_data(random_film('ужасы'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='horror_ran')
    elif c.data == "musical_ran":
        result = format_data(random_film('мюзикл'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='musical_ran')
    elif c.data == "mistery_ran":
        result = format_data(random_film('детектив'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='mistery_ran')
    elif c.data == "romance_ran":
        result = format_data(random_film('мелодрама'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='romance_ran')
    elif c.data == "sci_fi_ran":
        result = format_data(random_film('фантастика'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='sci_fi_ran')
    elif c.data == "war_ran":
        result = format_data(random_film('военный'))
        again = types.InlineKeyboardButton(text='Повторить', callback_data='war_ran')
    elif c.data == "back":
        msg = bot.send_message(cid, 'You are on the main menu')
        bot.register_next_step_handler(msg, send_welcome)
    elif c.data == 'add_wishlist':
        print(result)
        # add_to_wishlist(print_id_list()[0])
    keyboard.add(again, back)
    keyboard_wishlist = types.InlineKeyboardMarkup()
    add_wishlist = types.InlineKeyboardButton(text='Добавить в Избранное \U0001F4CD', callback_data='add_wishlist')
    keyboard_wishlist.add(add_wishlist)
    if len(result[0]) != 0:
        for elem in result[0]:
            bot.send_message(cid, ''.join(elem), reply_markup=keyboard_wishlist)
        bot.send_message(cid, 'Предложить еще фильмов?', reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'Новинки \U0001F31F':
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        again = types.InlineKeyboardButton(text='Повторить', callback_data='back')
        keyboard.add(again, back)
        result = format_data(new_films())
        keyboard_wishlist = types.InlineKeyboardMarkup()
        add_wishlist = types.InlineKeyboardButton(text='Добавить в Избранное \U0001F4CD', callback_data='add_wishlist')
        keyboard_wishlist.add(add_wishlist)
        for elem in result[0]:
            bot.send_message(message.chat.id, ''.join(elem), reply_markup=keyboard_wishlist)
        bot.send_message(message.chat.id, 'Предложить еще фильмов?', reply_markup=keyboard)

    elif message.text == 'Рекомендации фильмов \U0001F378':
        markup_genre = types.InlineKeyboardMarkup()
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
        back = types.InlineKeyboardButton(text='Назад в меню', callback_data='back')
        markup_genre.add(action, adventure, comedy, crime, drama, fantasy, history, horror, musical, mistery, romance, sci_fi, war, back)
        bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup_genre)

    elif message.text == 'Лучшие из лучших \U0001F525':
        keyboard = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        again = types.InlineKeyboardButton(text='Повторить', callback_data='back')
        keyboard.add(again, back)
        result = format_data(best_of_the_best())
        keyboard_wishlist = types.InlineKeyboardMarkup()
        add_wishlist = types.InlineKeyboardButton(text='Добавить в Избранное \U0001F4CD', callback_data='add_wishlist')
        keyboard_wishlist.add(add_wishlist)
        for elem in result[0]:
            bot.send_message(message.chat.id, ''.join(elem), reply_markup=keyboard_wishlist)
        bot.send_message(message.chat.id, 'Предложить еще фильмов?', reply_markup=keyboard)

    elif message.text == 'Рандомный фильм \U0001F3AC':
        markup_genre = types.InlineKeyboardMarkup()
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
        back = types.InlineKeyboardButton(text='Назад в меню', callback_data='back')
        markup_genre.add(action, adventure, comedy, crime, drama, fantasy, history, horror, musical, mistery, romance,sci_fi, war, back)
        bot.send_message(message.chat.id, "Выберите жанр:", reply_markup=markup_genre)

    elif message.text == 'Посмотреть Избранное \U0001F4CD':
        for elem in wishlist:
            bot.send_message(message.chat.id, ''.join(elem))

bot.infinity_polling()
