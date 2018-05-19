import dc_comic
def main():
    dc_comic.init()
    print("DC COMIC CHARACTERS")
    print()

    hero = dc_comic.search(name='Batman')
    print(hero)




if __name__ == '__main__':
    main()