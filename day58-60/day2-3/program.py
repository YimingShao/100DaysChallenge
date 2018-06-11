import api

def main():
    name_set=[]
    sig_set=[]
    api.friends_set(name_set,sig_set)
    api.show_cloud(name_set)

if __name__ == '__main__':
    main()
