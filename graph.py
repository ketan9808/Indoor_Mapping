from collections import defaultdict

def create_graph():
    graph = defaultdict(list)
    while 1:
        print('Enter the parent node and all of its Ist generation child separated by space ', end = ':')
        parent, *child = input().upper().split(' ')
        graph[parent] = child
        print('any node left ', end = ':')
        k = input()[0].upper()
        if k=='Q':
            break
    return graph

def find_all_paths(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths