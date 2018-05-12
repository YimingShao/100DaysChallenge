from Binary_Search_Tree import Node
import random
def main():
    Dict = ['Dog', 'Cat', 'Flamingo', 'Donkey', 'Fish', 'Seagull', 'Elephant', 'Panda',
            'Kiwi', 'Wolf', 'Fox', 'Blue whale', 'Weasel', 'Pigeon']
    root = Node(12, 'Tiger')
    num_list = [i for i in range(1,15)]
    num_list.remove(12)

    for i in range(1, 14):
        k = random.choice(num_list)
        num_list.remove(k)
        v = random.choice(Dict)
        Dict.remove(v)
        root.insert(k, v)

    dict = {}
    root.fill_in_dict(dict)
    for k,v in dict.items():
        print (k, v)
    root.delete(8)

    dict = {}
    root.fill_in_dict(dict)
    print('\n\n\n')
    for k,v in dict.items():
        print (k, v)






if __name__ == '__main__':
    main()