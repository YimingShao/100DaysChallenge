import re
from collections import Counter


def main():
    # when_not_use_regexes()
    # Comparing_re_search_and_re_match()
    # String_capturing_parenthesis()
     find_all_is_your_friend()
    #   Compiling_regexes()



def when_not_use_regexes(text):
    print1 = str(text.startswith('Awesome'))
    print2 = str(text.endswith('challenge'))
    print3 = str('100daysofcode' in text.lower())
    print4 = str(text.replace('100', '200'))

    print('startswith:\n' + print1)
    print()
    print('endswith:\n' + print2)
    print()
    print('Does text contain \'100daysofcode\':\n' + print3)
    print()
    print('Replace 100 with 200:\n' + print4)
    print()


def Comparing_re_search_and_re_match():
    text = 'Awesome, I am doing the #100DaysOfCode challenge'
    print1 = str(re.search(r'I am', text))
    print2 = str(re.match(r'I am', text))
    print3 = str(re.match(r'Awesome.*challenge', text))

    print('Search use r:\n' + print1)
    print()
    print('Match use r:\n' + print2)
    print()
    print('Try match again:\n' + print3)
    print()


def String_capturing_parenthesis():
    hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
    two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'


    print1 = re.match(r'.*(#\d+DaysOfCode).*', hundred)
    print2 = re.search(r'(#\d+DaysOfCode)', two_hundred)


    print('Capturing strings by match:\n'+str(print1))
    print(print1.groups()[0])
    print()
    print('Capturing strings by search:\n'+str(print2))
    print(print2.groups()[0])
    print()

def find_all_is_your_friend():
    text1 = '''
    $ python module_index.py |grep ^re
    re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
    '''
    text2 = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
    the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
    scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
    electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
    Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
    PageMaker including versions of Lorem Ipsum'''

    print1 = re.findall(r'\d+',text1)
    print2 = re.findall(r'\w+',text2)
    print2 = text2.split()[:5]
    print3 = Counter(re.findall(r'[A-Z][a-z0-9]+',text2))

    print('Find all:\n'+str(print1))
    print()
    print('Split:\n'+str(print2))
    print()
    print('Find word:\n'+str(print3))
    print(print3.most_common(5))
    print()


def Compiling_regexes():
    movies = '''1. Citizen Kane (1941)
    2. The Godfather (1972)
    3. Casablanca (1942)
    4. Raging Bull (1980)
    5. Singin' in the Rain (1952)
    6. Gone with the Wind (1939)
    7. Lawrence of Arabia (1962)
    8. Schindler's List (1993)
    9. Vertigo (1958)
    10. The Wizard of Oz (1939)'''.split('\n')

    pat = re.compile(r'''^\d+\.\s+(?:[A-Za-z']+\s){2}\(\d{4}\)$''', re.VERBOSE)
    for movie in movies:
        print(movie, pat.match(movie))


if __name__ == '__main__':
    main()
