from lib import (Depth_First_Search, Breadth_First_Search)

def main():
    DFS_graph = {'A': set(['B', 'D', 'E', 'C']),
             'B': set(['A', 'C']),
             'C': set(['A', 'B', 'D', 'E']),
             'D': set(['A', 'C']),
             'E': set(['A', 'C']),}


    BFS_graph = {'A': set(['B', 'C', 'D']),
             'B': set(['A', 'E', 'C']),
             'C': set(['A', 'B', 'D', 'E', 'F']),
             'D': set(['A', 'C', 'F']),
             'E': set(['B', 'C', 'F']),
             'F': set(['C', 'D'])}
    visited = Depth_First_Search(DFS_graph, 'A', [], [])
    print('DFS:\n'+str(visited))
    print()
    visited = Breadth_First_Search(BFS_graph, 'A')
    print('BFS:\n'+str(visited))
    print()

if __name__ == '__main__':
    main()
