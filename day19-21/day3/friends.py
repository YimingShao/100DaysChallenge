from itertools import permutations, combinations


def main():
    friends = 'Bob Dante Julian Martin'.split()
    print(friends_teams(friends, team_size=2, order_does_matter=True))

def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter is True:
        new_list = list(permutations(friends, team_size))
    else:
        new_list = list(combinations(friends, team_size))
    return new_list

if __name__ == '__main__':
    main()