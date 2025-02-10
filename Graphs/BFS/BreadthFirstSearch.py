def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


def bfs_1(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=' ')

        for adj in graph[s]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)


def bfs_2(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        u = queue.pop(0)

        print(u, end=' ')

        for v in graph[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)


def bfs_3(graph, node):
    queue = []
    visited = []

    visited.append(node)
    queue.append(node)

    while queue:
        u = queue.pop(0)  # First in first out

        print(u, end=' ')

        for v in graph[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)


def bfs_4(node, graph):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:

        u = queue.pop(0)

        print(u, end=' ')
        for v in graph[u]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
