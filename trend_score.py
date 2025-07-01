import requests
from bs4 import BeautifulSoup
import subprocess
import json

# Load keywords
def load_keywords():
    with open("keywords.json", "r") as f:
        return json.load(f)

# Count mentions in news headlines
def count_in_news(keyword):
    url = 'https://www.coindesk.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('a', class_='card-title')
    
    count = 0
    for h in headlines:
        if keyword.lower() in h.get_text(strip=True).lower():
            count += 1
    return count

# Count tweets using snscrape
def count_in_tweets(keyword, max_results=30):
    command = f'snscrape --max-results {max_results} twitter-search "{keyword}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return len(result.stdout.splitlines())

# Combine both scores
def trend_score():
    data = load_keywords()
    result = {}

    for category, keywords in data.items():
        print(f"\n📊 {category.upper()} TRENDS")
        result[category] = {}
        for keyword in keywords:
            news_count = count_in_news(keyword)
            tweet_count = count_in_tweets(keyword)
            score = news_count * 2 + tweet_count  # Weighted score
            result[category][keyword] = score
            print(f"→ {keyword}: News={news_count}, Tweets={tweet_count}, Trend Score={score}")

    return result

if __name__ == "__main__":
    trend_score()
