import requests
from bs4 import BeautifulSoup

URL = 'https://habr.com/ru/all/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

text = requests.get(URL).text
soup = BeautifulSoup(text,'html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    hubs = []
    for h in article.find_all('a', class_='tm-article-snippet__hubs-item-link'):
        hubs.append(h.text.strip())

    headline = article.h2.a.text
    post_preview_text = article.div.div.text
    post_link = article.find('a', class_='tm-article-snippet__title-link')
    post_link = 'https://habr.com/'+ post_link.attrs.get('href')
    public_date = article.find('span', class_='tm-article-snippet__datetime-published').text

    for search_word in KEYWORDS:
        if (search_word.lower() in headline.lower()) or (search_word.lower() in post_preview_text.lower()):
            print(f'Дата: {public_date} - Заголовок: {headline} - Ссылка: {post_link}')