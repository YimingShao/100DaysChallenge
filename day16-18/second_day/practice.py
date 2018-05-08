import random

def main():
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
             'julian sequeira', 'sandra bullock', 'keanu reeves',
             'julbob pybites', 'bob belderbos', 'julian sequeira',
             'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
    new_list = make_title_case(NAMES)
    print(new_list)
    print(list(gen_pairs(NAMES)))

def make_title_case(list):
    new_list = [element.title() for element in list]
    return new_list

def gen_pairs(list):
    first_name_list = [name.title().split()[0] for name in list]
    while len(first_name_list)!=1:
        p1 = random.choice(first_name_list)
        first_name_list.remove(p1)
        p2 = random.choice(first_name_list)
        first_name_list.remove(p2)
        yield '{} teams up with {}'.format(p1,p2)

if __name__=='__main__':
    main()
