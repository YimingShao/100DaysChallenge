import feedparser
import webbrowser

def main():
    FEED_FILE = "toronto_news.xml"
    feed = feedparser.parse(FEED_FILE)


    if 'title' in feed.entries[0]:
        i=0
        for entry in feed.entries:
            i+=1
            print(f"{i}: {entry.title} + ':\n'+{entry.links[0]['href']}\n")

    key = int(input('Which news you want to view?\t'))

    try:
        webbrowser.open(feed.entries[key-1].links[0]['href'])
    except Exception as x:
        print(x)





if __name__ == '__main__':
    main()