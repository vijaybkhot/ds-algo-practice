def has_cycle(graph):
    visited = set()  # Set to keep track of visited vertices

    def dfs(vertex, parent):
        visited.add(vertex)  # Mark the current vertex as visited
        for neighbor in graph[vertex]:  # Iterate over neighbors of the current vertex
            if neighbor not in visited:  # If neighbor is not visited, recursively call dfs
                if dfs(neighbor, vertex):  # If dfs returns True, there is a cycle
                    return True
            elif neighbor != parent:  # If neighbor is visited and not the parent, there is a cycle
                return True
        return False  # If no cycle is found, return False

    for vertex in graph:  # Iterate over all vertices in the graph
        if vertex not in visited:  # If vertex is not visited, start a new dfs traversal
            if dfs(vertex, None):  # If dfs returns True, there is a cycle
                return True

    return False  # If no cycle is found after checking all vertices, return False


def has_cycle_1(graph):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if dfs(neighbour, vertex) == True:
                    return True
            elif neighbour in visited and neighbour != parent:
                return True

        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, parent=None) == True:
                return True
    return False


def has_cycle_2(graph):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if dfs(neighbour, parent) == True:
                    return True
            elif neighbour in visited and neighbour != parent:
                return True

        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, parent=None) == True:
                return True
    return False


def has_cycle_3(graph):
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                # Visit the neighbour and check if it is part of a cycle
                if dfs(neighbour, vertex) == True: return True
            elif neighbour in visited and neighbour != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, parent=None) == True: return True

    return False


def has_cycle_4(graph):
    visited = set()

    def dfs(vertex, parent, visited, graph):
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if dfs(neighbour, vertex, visited, graph) == True:
                    return True
            elif neighbour in visited and neighbour != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None, visited, graph) == True:
                return True
    return False


def has_cycle_5(graph):
    visited = set()

    def dfs(vertex, parent, visited, graph):
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if dfs(neighbour, vertex, visited, graph) == True:
                    return True
            elif neighbour in visited and neighbour != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None, visited, graph):
                return True
    return False


def has_cycle_6(graph):
    visited = set()

    def dfs(vertex, parent, graph):
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                if dfs(neighbour, vertex, graph) == True:
                    return True
            elif neighbour in visited and neighbour != parent:
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None, graph):
                return True
    return False


graph = {}
print(has_cycle_4(graph))  # Expected output: False

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}
print(has_cycle_4(graph))  # Expected output: False

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5]
}
print(has_cycle_4(graph))  # Expected output: True

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5, 6]
}
print(has_cycle_4(graph))  # Expected output: True

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 6],
    6: [5, 6]
}
print(has_cycle_4(graph))  # Expected output: True
