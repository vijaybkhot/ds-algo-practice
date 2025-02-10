def topological_sort(graph):
    stack = []
    visited = set()

    def dfs(u):
        visited.add(u)
        for neighbour in graph[u]:
            if neighbour not in visited:
                dfs(neighbour)
        stack.append(u)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]


def topsort(graph):
    stack = []
    visited = set()
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
            elif v in visited and v not in stack:  # If v is visited and not in stack, it's a back edge
                has_cycle = True

        stack.append(u)

    for u in graph:
        if u not in visited:
            dfs(u)
    if has_cycle:
        raise ValueError("Graph is cyclic. Topological sort not possible.")
    else:
        return stack[::-1]


def top_sort_1(graph):
    stack = []
    visited = set()
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
            elif v in visited and v not in stack:
                has_cycle = True
                return
        stack.append(u)

    for u in graph:
        if u not in visited:
            dfs(u)
    if has_cycle:
        raise ValueError("Graph is cyclic. Topological sort is not possible.")
    else:
        return stack[::-1]


def topsort_2(graph):
    stack = []
    visited = set()

    has_cycle = False

    def dfs(u, visited, stack):
        nonlocal has_cycle

        if u not in visited:
            visited.add(u)
            for v in graph[u]:
                if v not in visited:
                    dfs(v, visited, stack)
                elif v in visited and v not in stack:
                    has_cycle = True
                    return
            stack.append(u)

    for u in graph:
        if u not in visited:
            dfs(u, visited, stack)
    if has_cycle:
        raise ValueError("The graph is cyclic. Topological sort not possible.")
    else:
        return stack[::-1]


def topsort_3(graph):
    visited = set()
    stack = []

    has_cycle = False

    def dfs(vertex, visited, stack):
        nonlocal has_cycle
        if vertex not in visited:
            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    dfs(neighbour, visited, stack)
                elif neighbour in visited and neighbour not in stack:
                    has_cycle = True
                    return
            stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, visited, stack)

    if has_cycle:
        return "The graph is cyclic. Topological sort not possible."
    else:
        return stack[::-1]


def topsort_4(graph):
    visited = set()
    stack = []
    has_cycle = False

    def dfs(vertex, visited, stack):
        nonlocal has_cycle
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(neighbour, visited, stack)
            elif neighbour in visited and neighbour not in stack:
                has_cycle = True
                return
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, visited, stack)
    if has_cycle:
        return "The graph is cyclic. Topological sort is not possible."
    else:
        return stack[::-1]


def topsort_5(graph):
    visited = set()
    stack = []
    has_cycle = False

    def dfs(vertex, visited, stack):
        nonlocal has_cycle
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs(neighbour, visited, stack)
            elif neighbour in visited and neighbour not in stack:
                has_cycle = True
                return
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex, visited, stack)

    if has_cycle:
        return "The graph is cyclic. Topological sort not possible."
    else:
        return stack[::-1]


def topsort_6(graph):
    visited = set()
    stack = []
    has_cycle = False

    def dfs_topsort(vertex, visited, stack):
        nonlocal has_cycle
        visited.add(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dfs_topsort(neighbour, visited, stack)
            elif neighbour in visited and neighbour not in stack:
                has_cycle = True
                return
        stack.append(vertex)

    for vertex in graph:
        if vertex not in visited:
            dfs_topsort(vertex, visited, stack)

    if has_cycle:
        return "The graph is Directed cyclic. Topological sort is not possible."
    else:
        return stack[::-1]


# Example usage
def test_topsort(topsort):
    graph = {
        'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }

    print(topsort(graph))

    graph_acyclic = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    print(topsort(graph_acyclic))  # Expected output: [1, 3, 2, 4] or [1, 2, 3, 4]

    graph_single_node = {
        1: []
    }
    print(topsort(graph_single_node))  # Expected output: [1]

    graph_empty = {}
    print(topsort(graph_empty))  # Expected output: []

    graph_cyclic = {
        1: [2],
        2: [3],
        3: [1]
    }
    print(topsort(graph_cyclic))  # Expected output: None or Error (Graph has a cycle)

    graph_multiple_components = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': [],
        'D': ['E'],
        'E': []
    }
    print(topsort(graph_multiple_components))  # Expected output: ['D', 'E', 'A', 'B', 'C'] or ['D', 'E', 'B', 'C', 'A']

    graph_large_acyclic = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [7],
        5: [7],
        6: [],
        7: []
    }
    print(topsort(graph_large_acyclic))  # Expected output: [1, 3, 6, 2, 5, 4, 7] or [1, 2, 3, 4, 5, 6, 7]

    graph_self_loops = {
        'A': ['A', 'B'],
        'B': ['C'],
        'C': []
    }
    print(topsort(graph_self_loops))  # Expected output: None or Error (Graph has a cycle)


test_topsort(topsort_6)
