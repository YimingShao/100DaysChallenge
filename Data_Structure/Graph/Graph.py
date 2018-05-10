from lib import (Depth_First_Search, Breadth_First_Search)

def main():
    graph = {'A': set(['B', 'D', 'E']),
             'B': set(['A', 'C']),
             'C': set(['A', 'B', 'D', 'E']),
             'D': set(['A', 'C']),
             'E': set(['A', 'C']),}
    visited = Depth_First_Search(graph, 'A', [], [])
    #print('DFS:\n'+str(visited))
    print()
    visited = Breadth_First_Search(graph, 'A')
    print('BFS:\n'+str(visited))
    print()

if __name__ == '__main__':
    main()
