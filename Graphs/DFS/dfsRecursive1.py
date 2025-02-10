# Example graph representation using adjacency lists
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

visited = set()


def dfs_recursive(at, visited, graph):
    if at not in visited:
        visited.add(at)
        for neighbour in graph[at]:
            dfs_recursive(neighbour, visited, graph)


def dfs_recursive_2(at, visited, graph):
    if at not in visited:
        visited.add(at)
        for neighbour in graph[at]:
            dfs_recursive_2(neighbour, visited, graph)


def dfs_recursive_3(at, visited, graph):
    if at not in visited:
        visited.add(at)
        for neighbour in graph[at]:
            dfs_recursive_3(neighbour, visited, graph)

def dfs_recursive_4(at, visited, graph):
    if at not in visited:
        visited.add(at)
        for neighbour in graph[at]:
            dfs_recursive_4(at, visited, graph)

