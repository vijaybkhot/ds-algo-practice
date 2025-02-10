from collections import deque


def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node)
    while stack:
        s = stack.pop()
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


# Example graph representation using adjacency lists
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Initialize the visited array
visited = [False] * len(graph)


def dfs_recursive(at):
    if visited[at]:
        return
    else:
        visited[at] = True

    neighbours = graph[at]
    for nxt in neighbours:
        dfs_recursive(nxt)



def dfs_recursive_1(at):
    if visited[at]:
        return
    else:
        visited[at] = True

    neighbours = graph[at]
    for nxt in neighbours:
        dfs_recursive(nxt)


# Starting DFS from node 2
dfs_recursive(2)

# Print the visited array to see which nodes were visited
print(visited)
