import requests
import collections
from typing import List

Result_list=collections.namedtuple('Result', 'category, id, url, title, description')

def search_by_keyword(keyword:str)->List[Result_list]:
    url=f'http://search.talkpython.fm/api/search?q={keyword}'
    data=requests.get(url)
    data.raise_for_status()

    my_data=data.json()
    resuluts=[]
    for r in my_data.get('results'):
        resuluts.append(Result_list(**r))
    return resuluts