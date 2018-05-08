def main():
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
             'julian sequeira', 'sandra bullock', 'keanu reeves',
             'julbob pybites', 'bob belderbos', 'julian sequeira',
             'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

    bites = {6: 'PyBites Die Hard',
             7: 'Parsing dates from logs',
             9: 'Palindromes',
             10: 'Practice exceptions',
             11: 'Enrich a class with dunder methods',
             12: 'Write a user validation function',
             13: 'Convert dict in namedtuple/json',
             14: 'Generate a table of n sequences',
             15: 'Enumerate 2 sequences',
             16: 'Special PyBites date generator',
             17: 'Form teams from a group of friends',
             18: 'Find the most common wexcludeord',
             19: 'Write a simple property',
             20: 'Write a context manager',
             21: 'Query a nested data structure'}
    exclude_bites = {6, 10, 16, 18, 21}

    new_dict = filter_bites(bites, exclude_bites)
    print(new_dict)

    new_list = dedup_and_title_case_names(NAMES)
    print(new_list)
    new_list2 = sort_by_surname_desc(new_list)
    print(new_list2)
    shortest_name = shortest_first_name(new_list)
    print(shortest_name)


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    new_list = list({name.title() for name in names})
    return new_list;


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    new_list = sorted(names, key=lambda n: n.split()[1])
    return new_list
    # ...


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    new_list = list({name.split()[0] for name in names})
    shortest_name = min(new_list,key=str )
    return shortest_name
    # ...

def filter_bites(bites, bites_done):
    """return the bites dict with the exclude_bites filtered out"""
    new_dict = {k:v for k, v in bites.items() if k not in bites_done}
    return new_dict


if __name__=='__main__':
    main()