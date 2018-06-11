import itchat
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from wordcloud import WordCloud
import api
import jieba

my_font = '/Library/Fonts/songti.ttc'
itchat.auto_login()

def friends_set(name_set, signature_set):

    friend_list = itchat.get_friends(update=True)[0:]
    for friend in friend_list:
        name_set.append(friend['NickName'])
        if friend['Signature']:
            signature_set.append(friend['Signature'])

def show_cloud(set):

    text = ''.join(set)
    wordlist = jieba.cut(text, cut_all=True)
    word_space_split = " ".join(wordlist)

    pb_mask = np.array(Image.open("pic.jpg"))
    wc = WordCloud(font_path=my_font,
                   background_color="white", max_font_size=100,
                   min_font_size=38,max_words=5000, mask=pb_mask,scale=1)
    wc.generate(word_space_split)
    plt.figure(figsize=(55, 55))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()