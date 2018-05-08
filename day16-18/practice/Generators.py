import calendar
import timeit
from pprint import pprint as pp


def num_gen():
    for i in range(5):
        yield i
gen = num_gen()
print(next(gen))

for i in gen:
    print(i)

options = 'red yellow blue white black green purpose'.split()
print(options)

def create_select_options(options=options):
    select_list = []

    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')
    return select_list

pp(create_select_options())

print('Generate version\n')


def create_select_options_gen(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'

print(list(create_select_options_gen()))


#list
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1,n+1):
        if calendar.isleep(year):
            leap_years.append(year)
        return leap_years

#generator
def leap_years_gen(n=100000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield  year

