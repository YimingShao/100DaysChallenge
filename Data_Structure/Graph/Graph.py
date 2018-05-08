from DFS import Depth_First_Search
def main():
    graph = {'A': set(['B', 'D', 'E']),
             'B': set(['A', 'C']),
             'C': set(['A', 'B', 'D', 'E']),
             'D': set(['A', 'C']),
             'E': set(['A', 'C']),}
    visited = Depth_First_Search(graph, 'A', [], [])
    print(visited)

if __name__ == '__main__':
    main()
