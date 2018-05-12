
def main():
    table = build_table(Size=10)
    print(table)
    insert(table, 15, 'dog')
    insert(table, 115, 'cat')
    print(table)


def build_table(Size=10):
    table = [[] for i in range(0, Size)]
    return table

def hashing(x, N=10):
    return x % N

def insert(table, key, value):
    table[hashing(key)].append(value)


if __name__ == '__main__':
    main()