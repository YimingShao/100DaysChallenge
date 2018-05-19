import os
import csv
from typing import List
import collections


data = []
Record = collections.namedtuple(
    'Record',
    'page_id,name,urlslug,ID,ALIGN,EYE,HAIR,SEX,GSM,ALIVE,APPEARANCES,FIRST APPEARANCE,YEAR'
)

def init():

    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'dc_characters.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            data.append(row)



def search(name=None):
    for character in data:
        if name.lower() in character['name'].lower():
            return character

    return ('No such person')








