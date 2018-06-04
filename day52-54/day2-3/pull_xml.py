import requests

URL = "https://toronto.ctvnews.ca/rss/ctv-news-toronto-1.822319"

if __name__ == '__main__':
    r = requests.get(URL)

    with open('toronto_news.xml','wb') as f:
        f.write(r.content)