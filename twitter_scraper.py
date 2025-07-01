import subprocess
import json

def load_keywords():
    with open("keywords.json", "r") as f:
        return json.load(f)

def search_tweets(keyword, max_results=10):
    command = f'snscrape --max-results {max_results} twitter-search "{keyword}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.splitlines()

def main():
    keywords = load_keywords()
    result_data = {}

    for category, word_list in keywords.items():
        result_data[category] = {}
        print(f"\n🔍 {category.upper()} TRENDS:")
        for word in word_list:
            tweets = search_tweets(word)
            count = len(tweets)
            result_data[category][word] = count
            print(f"→ {word}: {count} tweets")

    return result_data

if __name__ == "__main__":
    main()
