import itertools
import os
import urllib.request

# PREWORK

DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
def main():
    draw = ['a', 'b', 'c', 'p', 'd', 'o']
    words1=_get_permutations_draw(draw)
    print(list(words1))
    words = get_possible_dict_words(draw)
    print(words)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    new_words = _get_permutations_draw(draw)
    sub_new_word = [word for word in new_words if word in dictionary]
    return sub_new_word

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    main_part=[]
    for i in range(2, len(draw)+1):
        sub_part = itertools.permutations(draw,i)
        for sub_part_word in sub_part:
            main_part.append(''.join(sub_part_word).lower())
    return main_part


if __name__ == '__main__':
    main()
