import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

from api import Twitter


account_name = "Yang55109999"

twitter = Twitter(account_name)
twitter.connect()

tweets = twitter.get_tweets()

sorted_tweets = twitter.sort_by_popularity()

fmt = '{likes:<5} | {rts: <5} | {text}'
print(fmt.format(likes='♥', rts='♺', text='✍'))
print('-' * 100)
for tw in sorted_tweets[:10]:
    print(fmt.format(likes=tw.likes, rts=tw.rts,
                     text=tw.text.replace('\n', '⏎')))

all_tweets_excl_rts_mentions = ' '.join(
    [tw.text.lower() for tw in tweets if not tw.text.startswith('RT') and not
     tw.text.startswith('@')]
)

pb_mask = np.array(Image.open("pybites.png"))
stopwords = set(STOPWORDS)
stopwords.add('co')
stopwords.add('https')

wc = WordCloud(background_color='white', max_words=2000, mask=pb_mask,
               stopwords=stopwords)

wc.generate(all_tweets_excl_rts_mentions)


plt.figure(figsize=(15, 15))
plt.imshow(wc, interpolation="bilinear")
plt.margins(x=0, y=0)
plt.axis("off")

plt.show()