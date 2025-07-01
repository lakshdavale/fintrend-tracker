import requests
from bs4 import BeautifulSoup

def get_crypto_news():
    url = 'https://www.coindesk.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('a', class_='card-title')  # May need update
    news = []

    for h in headlines[:10]:
        news.append(h.get_text(strip=True))

    return news

if __name__ == '__main__':
    print("📰 Trending Crypto News:")
    for headline in get_crypto_news():
        print("→", headline)
