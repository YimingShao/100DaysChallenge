# Pre: Graph is a connected graph


def Depth_First_Search(graph, vertex, known, forest):

    # Mark vertex u as visited
    known.append(vertex)

    # Check each of u's outgoing edges, e
    for e in graph[vertex]:
        # If e has not been visited, add to forest
        if e not in known:
            forest.append(e)
            Depth_First_Search(graph, e, known, forest)
    return known


def Breadth_First_Search(graph, root):
    visited, queue = set(),[root]
    while queue:
        print('Beginning: ' + str(queue))
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print('Visited: '+str(visited))

            queue.extend(graph[vertex]-visited)
            print('Ending: ' +str(queue)+'\n\n\n')
    return visited