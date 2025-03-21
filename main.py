import telebot
from telebot import types
from hooks import send_request, format_data, random_film, new_films, best_of_the_best

API_TOKEN = '7818305458:AAHql1NDOblTnOy48LjLDhue-mrjWc2PsDQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    new_film = types.KeyboardButton('New films')
    recommend_film = types.KeyboardButton('Movie recommendation')
    best_films = types.KeyboardButton('Best of the best')
    film_random = types.KeyboardButton('Random movie')
    markup.add(new_film, recommend_film, best_films, film_random)
    bot.send_message(message.chat.id, "Hello! I'm your Movie Bot. Press any button and I will help you choose a film.", reply_markup=markup)


@bot.callback_query_handler(func=lambda c:True)
def ans(c):
    cid = c.message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='Back', callback_data='back')
    again = types.InlineKeyboardButton(text='Again', callback_data='back')
    result = []
    if c.data == "action_rec":
        result = format_data(send_request('action'))
        again = types.InlineKeyboardButton(text='Again', callback_data='action_rec')
    elif c.data == "adventure_rec":
        result = format_data(send_request('adventure'))
        again = types.InlineKeyboardButton(text='Again', callback_data='adventure_rec')
    elif c.data == "comedy_rec":
        result = format_data(send_request('comedy'))
        again = types.InlineKeyboardButton(text='Again', callback_data='comedy_rec')
    elif c.data == "crime_rec":
        result = format_data(send_request('crime'))
        again = types.InlineKeyboardButton(text='Again', callback_data='crime_rec')
    elif c.data == "drama_rec":
        result = format_data(send_request('drama'))
        again = types.InlineKeyboardButton(text='Again', callback_data='drama_rec')
    elif c.data == "fantasy_rec":
        result = format_data(send_request('fantasy'))
        again = types.InlineKeyboardButton(text='Again', callback_data='fantasy_rec')
    elif c.data == "history_rec":
        result = format_data(send_request('history'))
        again = types.InlineKeyboardButton(text='Again', callback_data='history_rec')
    elif c.data == "horror_rec":
        result = format_data(send_request('horror'))
        again = types.InlineKeyboardButton(text='Again', callback_data='horror_rec')
    elif c.data == "musical_rec":
        result = format_data(send_request('musical'))
        again = types.InlineKeyboardButton(text='Again', callback_data='musical_rec')
    elif c.data == "mistery_rec":
        result = format_data(send_request('mistery'))
        again = types.InlineKeyboardButton(text='Again', callback_data='mistery_rec')
    elif c.data == "romance_rec":
        result = format_data(send_request('romance'))
        again = types.InlineKeyboardButton(text='Again', callback_data='romance_rec')
    elif c.data == "sci_fi_rec":
        result = format_data(send_request('sci-fi'))
        again = types.InlineKeyboardButton(text='Again', callback_data='sci_fi_rec')
    elif c.data == "war_rec":
        result = format_data(send_request('war'))
        again = types.InlineKeyboardButton(text='Again', callback_data='war_rec')

    elif c.data == "action_ran":
        result = format_data(random_film('action'))
        again = types.InlineKeyboardButton(text='Again', callback_data='action_ran')
    elif c.data == "adventure_ran":
        result = format_data(random_film('adventure'))
        again = types.InlineKeyboardButton(text='Again', callback_data='adventure_ran')
    elif c.data == "comedy_ran":
        result = format_data(random_film('comedy'))
        again = types.InlineKeyboardButton(text='Again', callback_data='comedy_ran')
    elif c.data == "crime_ran":
        result = format_data(random_film('crime'))
        again = types.InlineKeyboardButton(text='Again', callback_data='crime_ran')
    elif c.data == "drama_ran":
        result = format_data(random_film('drama'))
        again = types.InlineKeyboardButton(text='Again', callback_data='drama_ran')
    elif c.data == "fantasy_ran":
        result = format_data(random_film('fantasy'))
        again = types.InlineKeyboardButton(text='Again', callback_data='fantasy_ran')
    elif c.data == "history_ran":
        result = format_data(random_film('history'))
        again = types.InlineKeyboardButton(text='Again', callback_data='history_ran')
    elif c.data == "horror_ran":
        result = format_data(random_film('horror'))
        again = types.InlineKeyboardButton(text='Again', callback_data='horror_ran')
    elif c.data == "musical_ran":
        result = format_data(random_film('musical'))
        again = types.InlineKeyboardButton(text='Again', callback_data='musical_ran')
    elif c.data == "mistery_ran":
        result = format_data(random_film('mistery'))
        again = types.InlineKeyboardButton(text='Again', callback_data='mistery_ran')
    elif c.data == "romance_ran":
        result = format_data(random_film('romance'))
        again = types.InlineKeyboardButton(text='Again', callback_data='romance_ran')
    elif c.data == "sci_fi_ran":
        result = format_data(random_film('sci-fi'))
        again = types.InlineKeyboardButton(text='Again', callback_data='sci_fi_ran')
    elif c.data == "war_ran":
        result = format_data(random_film('war'))
        again = types.InlineKeyboardButton(text='Again', callback_data='war_ran')
    elif c.data == "back":
        msg = bot.send_message(cid, 'You are on the main menu')
        bot.register_next_step_handler(msg, send_welcome)
    keyboard.add(again, back)
    if len(result) != 0:
        for elem in result:
            bot.send_message(cid, ''.join(elem))
            bot.send_message(cid, 'Would you like to do it again?', reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'New films':
        result = format_data(new_films())
        for elem in result:
            bot.send_message(message.chat.id, ''.join(elem))

    elif message.text == 'Movie recommendation':
        markup_genre = types.InlineKeyboardMarkup()
        action = types.InlineKeyboardButton(text='Action \U0001F4A5', callback_data='action_rec')
        adventure = types.InlineKeyboardButton(text='Adventure \U0001F9D7', callback_data='adventure_rec')
        comedy = types.InlineKeyboardButton(text='Comedy \U0001F639', callback_data='comedy_rec')
        crime = types.InlineKeyboardButton(text='Crime \U0001FA78', callback_data='crime_rec')
        drama = types.InlineKeyboardButton(text='Drama \U0001F3AD', callback_data='drama_rec')
        fantasy = types.InlineKeyboardButton(text='Fantasy \U0001F9DD', callback_data='fantasy_rec')
        history = types.InlineKeyboardButton(text='History \U0001F5E1', callback_data='history_rec')
        horror = types.InlineKeyboardButton(text='Horror \U0001F9DF', callback_data='horror_rec')
        musical = types.InlineKeyboardButton(text='Musical \U0001F3B6', callback_data='musical_rec')
        mistery = types.InlineKeyboardButton(text='Mistery \U0001F50E', callback_data='mistery_rec')
        romance = types.InlineKeyboardButton(text='Romance \U0001F48F', callback_data='romance_rec')
        sci_fi = types.InlineKeyboardButton(text='Sci-fi \U0001F47D', callback_data='sci_fi_rec')
        war = types.InlineKeyboardButton(text='War \U0001F93C', callback_data='war_rec')
        back = types.InlineKeyboardButton(text='Back to menu', callback_data='back')
        markup_genre.add(action, adventure, comedy, crime, drama, fantasy, history, horror, musical, mistery, romance, sci_fi, war, back)
        bot.send_message(message.chat.id, "Choose a genre:", reply_markup=markup_genre)

    elif message.text == 'Best of the best':
        result = format_data(best_of_the_best())
        for elem in result:
            bot.send_message(message.chat.id, ''.join(elem))

    elif message.text == 'Random movie':
        markup_genre = types.InlineKeyboardMarkup()
        action = types.InlineKeyboardButton(text='Action \U0001F4A5', callback_data='action_ran')
        adventure = types.InlineKeyboardButton(text='Adventure \U0001F9D7', callback_data='adventure_ran')
        comedy = types.InlineKeyboardButton(text='Comedy \U0001F639', callback_data='comedy_ran')
        crime = types.InlineKeyboardButton(text='Crime \U0001FA78', callback_data='crime_ran')
        drama = types.InlineKeyboardButton(text='Drama \U0001F3AD', callback_data='drama_ran')
        fantasy = types.InlineKeyboardButton(text='Fantasy \U0001F9DD', callback_data='fantasy_ran')
        history = types.InlineKeyboardButton(text='History \U0001F5E1', callback_data='history_ran')
        horror = types.InlineKeyboardButton(text='Horror \U0001F9DF', callback_data='horror_ran')
        musical = types.InlineKeyboardButton(text='Musical \U0001F3B6', callback_data='musical_ran')
        mistery = types.InlineKeyboardButton(text='Mistery \U0001F50E', callback_data='mistery_ran')
        romance = types.InlineKeyboardButton(text='Romance \U0001F48F', callback_data='romance_ran')
        sci_fi = types.InlineKeyboardButton(text='Sci-fi \U0001F47D', callback_data='sci_fi_ran')
        war = types.InlineKeyboardButton(text='War \U0001F93C', callback_data='war_ran')
        back = types.InlineKeyboardButton(text='Back to menu', callback_data='back')
        markup_genre.add(action, adventure, comedy, crime, drama, fantasy, history, horror, musical, mistery, romance,sci_fi, war, back)
        bot.send_message(message.chat.id, "Choose a genre:", reply_markup=markup_genre)

bot.infinity_polling()
