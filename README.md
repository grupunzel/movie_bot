<h1>Telegram Bot MovieBot</h1>
<div align='center'>
  <img src="https://static10.tgstat.ru/channels/_0/cf/cfc09bd1df9a6c9b386560c72e5170df.jpg" alt='telebram-bot' width='250' height='250'>
</div>

<h2>Documentation</h2>
Formal documentation for the library that is used in this project you can <a href='https://docs.python-telegram-bot.org/en/stable/index.html'>view here</a>.<br><br>
API token was taken from <a href='https://kinopoiskapiunofficial.tech/documentation/api/?ysclid=m9mioyr2y6157520274'>here</a>.

<h2>About the project</h2>
MovieBot is a Telegram bot that advises movies according to a genre you choose. Its recomendations are also based on the IMDb 
rating, so only high-quality movies will be shown. Additionaly, the bot provides full information about each movie, including 
the original name, year of release, ratings on Kinopoisk and IMDb, country, genre, description, poster, and trailer.
<br><br>
One of the useful features of the bot is ability to add movies to your wishlist. There is no limit to the number of films 
in the wishlist. You can also delete a movie from your wishlist.

<h2>Get started</h2>
To test the bot you can scan the QR code below or go to this <a href='https://t.me/LiveLikeInAMovieBot'>link</a>.
<br><br><img src='image0.jpeg' width='200' height='200'><br>
If you want to customize the code, use this instruction:<br><br>
1. Create a directory on your computer and copy there two files: 'main.py' and 'hooks.py'.<br><br>
2. Open the Command Prompt and go to the directory with the code, then install the virtual environment by running this code:<br><br>
<pre>
  python -m venv env
</pre><br>
3. Set the virtual environment. Go to the directory 'env', then 'Scripts', run 'activate', and go back to the directory with the project.<br><br>
4. In the Command Prompt install the library 'python-telegram-bot' by running this code:<br><br>
<pre>
pip install python-telegram-bot
</pre><br>
5. If you are using Visual Studio Code or PyCharm, do the same thing in the app terminal.<br><br>
6. Make your changes in the code.<br><br>
7. To test the code run the 'main.py' file in the Command Prompt:<br><br>
<pre>
  C:\your_repository>main.py
</pre>

<h2>Features</h2>
The bot menu includes five buttons:<br><br>
- <b>Новинки</b>:<br>
  The bot sends new films with release years not earlier than 2024.<br><br>
- <b>Рекомендации фильмов</b>:<br>
  The bot will send you a menu for genre selection. Choose a genre, and the bot will provide you five film recommendations.<br><br>
- <b>Лучшие из лучших</b>:<br>
  The bot sends the most popular films of all times with the highest IMDb rating.<br><br>
- <b>Рандомный фильм</b>:<br>
  The bot will send you a menu for genre selection. After choosing a genre, the bot will provide a random film with the selected genre.<br><br>
- <b>Посмотреть Избранное</b>:<br>
  The bot will display your wishlist. In this feature you can delete a film from your wishlist.<br><br>

<h2>Attached files</h2>
<ul>
  <li>
    <b>main.py</b> - file with bot interaction functions
  </li>
  <li>
    <b>hooks.py</b> - file with API interactions
  </li>
  <li>
    <b>links</b> - file with API link
  </li>
</ul>
