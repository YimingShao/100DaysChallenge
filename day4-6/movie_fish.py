import csv
import sys
import os.path
from collections import defaultdict, namedtuple

MOVIE_CSV = 'movie_metadata.csv'
Movie = namedtuple('Movie', 'title year score avg')


def main():

    if os.path.isfile(MOVIE_CSV):
        directors = get_movies_by_director()
        print('File loaded\n')
        print_instruction()
        key = rec_input()
        while key is not '4':
            if key is '1':
                search_by_name(directors)
            if key is '2':
                search_by_director(directors)
            if key is '3':
                search_by_year(directors)
            key = rec_input()
        quit_program()
    else:
        print('Loading failed\n')





def get_movies_by_director(data=MOVIE_CSV):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
                avg = float(0)
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score, avg=avg)
            directors[director].append(m)

    return directors


def rec_input():
    key = input("Insert: ")
    if key != '1' and key != '2' and key != '3' and key != '4' and key != '5':
        print('Please give the right instruction')
        rec_input()
    else:
        return key


def search_by_name(directors):
    movie_title = input('Enter the title: ')
    boo = False
    for key, values in directors.items():
        length = len(values)
        for i in range(length):
            if values[i].title.lower() == movie_title.lower():
                print('Movie '+values[i].title+' is made in '+str(values[i].year)+', by '+str(key) +', '+str(values[i].score)+'\n')
                boo = True
                break;
    if boo == False: print('Movie '+movie_title+' does not found\n')


def search_by_director(directors):
    director_name = input('Enter the name: ')
    boo = False
    for director, movies in directors.items():
        if director.lower()==director_name.lower():
            print(str(director)+':')
            for i in range(len(movies)):
                print(movies[i].title+'\t'+str(movies[i].year)+'\t'+str(movies[i].score))

            boo = True
            break
    if boo==False: print('No result about '+director_name)
    print('\n')



def search_by_year(directors):
    year = input('Year around: ')
    while year.isdigit() is False:
        print('Please enter a number')
        year = year = input('Year around: ')
    for director, movies in directors.items():
        for i in range(len(movies)):
            if(movies[i].year>int(year)-10 and movies[i].year<int(year)+10):
                print(
                    'Movie ' + movies[i].title + ' is made in ' + str(movies[i].year) + ', by ' + str(director) + ', ' + str(
                        movies[i].score) + '\n')
                boo = True
    boo = False
    if boo == False: print('No result around ' + str(year))
    print('\n')


def quit_program():
    print('-' *71  + '\n')
    print('Bye Bye!')
    print('\n' + '-' * 71)
    sys.exit()


def print_instruction():
    line = '-' * 30
    print(line + 'Instruction' + line)
    print('Insert 1: Search by movie name')
    print('Insert 2: Search by director')
    print('Insert 3: Search by year')
    print('Insert 4: Quit')

    print(line + line + '-' * 11)


if __name__ == '__main__':
    main()