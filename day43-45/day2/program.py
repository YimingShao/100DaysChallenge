import api

def main():
    menu()
    keyword= input('What keywords to search for?\t')
    results = api.search_by_keyword(keyword)

    print(f'There are {len(results)} matching episodes:')
    i=0
    for r in results:
        i+=1
        print(f"{i}. {r.title}")

def menu():
    print('******* SEARCH TALK PYTHON *******')
if __name__ == '__main__':
    main()