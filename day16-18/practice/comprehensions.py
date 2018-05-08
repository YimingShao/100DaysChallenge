from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

names = 'pybites mike bob julian tim sara guido'.split()
print(names)

for name in names:
    print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
print(first_half_alphabet)

new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
print(new_names)

new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]
assert new_names == new_names2
print(new_names)


resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
print(words[:5])

cnt = Counter(words)
print(cnt.most_common(5))
print('-' in words)

words = [re.sub(r'\W+', r'', word) for word in words]
print('-' in words)


resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
print(stopwords[:5])

words = [word for word in words if word.strip() and word not in stopwords]
print('the' in words)

cnt = Counter(words)
print(cnt.most_common(5))

