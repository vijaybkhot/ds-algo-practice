def has_cycle_sets(graph):
    white = set()
    gray = set()
    black = set()

    def dfs(current, white, gray, black, graph):
        move_vertex(current, white, gray)

        for neighbour in graph[current]:
            if neighbour in black:
                continue
            elif neighbour in gray:
                return True
            if dfs(neighbour, white, gray, black, graph):
                return True

        move_vertex(current, gray, black)
        return False

    def move_vertex(vertex, source_set, destination_set):
        source_set.remove(vertex)
        destination_set.add(vertex)

    for vertex in graph:
        white.add(vertex)

    while len(white) > 0:
        current = next(iter(white))
        if dfs(current, white, gray, black, graph) == True:
            return True
        else:
            return False


def has_cycle_sets_1(graph):
    white = set()
    gray = set()
    black = set()

    for vertex in graph:
        white.add(vertex)

    def move_vertex(node, source_set, destination_set):
        source_set.remove(node)
        destination_set.add(node)

    def dfs(vertex, white, gray, black, graph):
        move_vertex(vertex, white, gray)

        for neighbour in graph[vertex]:
            if neighbour in black:
                continue
            elif neighbour in gray:
                return True
            elif neighbour in white:
                if dfs(neighbour, white, gray, black, graph) == True:
                    return True
        move_vertex(vertex, gray, black)
        return False

    for vertex in graph:
        if vertex in white:
            if dfs(vertex, white, gray, black, graph):
                return True

    return False


def has_cycle_ses_2(graph):
    white = set()
    black = set()
    gray = set()

    def move_vertex(vertex, source, destination):
        source.remove(vertex)
        destination.add(vertex)

    def dfs(vertex, white, gray, black, graph):
        move_vertex(vertex, white, gray)

        for neighbour in graph[vertex]:
            if neighbour in white:
                if dfs(neighbour, white, gray, black, graph) == True:
                    return True
            elif neighbour in black:
                continue
            elif neighbour in gray:
                return True

        move_vertex(vertex, gray, black)
        return False

    for vertex in graph:
        white.add(vertex)

    for vertex in graph:
        if vertex in white:
            if dfs(vertex, white, gray, black, graph):
                return True

    return False


def detect_cycle_sets_3(graph):
    white = set()
    gray = set()
    black = set()

    def move_vertex(vertex, source, destination):
        source.remove(vertex)
        destination.add(vertex)

    def dfs(vertex, white, gray, black, graph):
        move_vertex(vertex, white, gray)

        for neighbour in graph[vertex]:
            if neighbour in white:
                if dfs(neighbour, white, gray, black, graph):
                    return True
            elif neighbour in black:
                continue
            elif neighbour in gray:
                return True
        move_vertex(vertex, gray, black)
        return False

    for vertex in graph:
        white.add(vertex)

    for vertex in graph:
        if vertex in white:
            if dfs(vertex, white, gray, black, graph):
                return True

    return False


def detect_cycle_sets_4(graph):
    def move_vertex(vertex, source_set, destination_set):
        source_set.remove(vertex)
        destination_set.add(vertex)

    def dfs(vertex, white, gray, black):
        move_vertex(vertex, white, gray)

        for neighbour in graph[vertex]:
            if neighbour in white:
                if dfs(neighbour, white, gray, black):
                    return True
            elif neighbour in gray:
                return True
            elif neighbour in black:
                continue

        move_vertex(vertex, gray, black)
        return False

    white = set()
    gray = set()
    black = set()

    for vertex in graph:
        white.add(vertex)

    for vertex in graph:
        if vertex in white:
            if dfs(vertex, white, gray, black):
                return True
    return False


def detect_cycle_sets_5(graph):
    def move_vertex(vertex, source_set, destination_set):
        source_set.remove(vertex)
        destination_set.add(vertex)

    def dfs(vertex, white, gray, black):
        move_vertex(vertex, white, gray)
        for neighbour in graph[vertex]:
            if neighbour in white:
                if dfs(neighbour, white, gray, black):
                    return True
            elif neighbour in gray:
                return True
            elif neighbour in black:
                continue
        move_vertex(vertex, gray, black)
        return False

    white = set()
    gray = set()
    black = set()

    for vertex in graph:
        white.add(vertex)

    for vertex in graph:
        if vertex in white:
            if dfs(vertex, white, gray, black):
                return True
    return False


def detect_cycle_sets_6(graph):
    white = set()
    gray = set()
    black = set()

    def move_vertex(vertex, source, destination):
        source.remove(vertex)
        destination.add(vertex)

    def dfs(vertex, white, gray, black):
        move_vertex(vertex, white, gray)

        for neighbour in graph[vertex]:
            if neighbour in black:
                continue
            elif neighbour in white:
                if dfs(neighbour, white, gray, black):
                    return True
            elif neighbour in gray:
                return True
        move_vertex(vertex, gray, black)
        return False

    for vertex in graph:
        white.add(vertex)

    for vertex in graph:
        if vertex in white:
            if dfs(vertex, white, gray, black):
                return True
    return False


graph_with_cycle = {
    1: [2],
    2: [3],
    3: [1]
}
graph_without_cycle = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}
graph_with_self_loop = {
    1: [2],
    2: [2]  # Self-loop on vertex 2
}
empty_graph = {}
graph_disconnected = {
    1: [2],
    2: [1],
    3: [4],
    4: [3]
}
large_graph_with_cycle = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [6],
    6: [1]
}
print(detect_cycle_sets_6(graph_with_cycle))  # Expected output: True
print(detect_cycle_sets_6(graph_without_cycle))  # Expected output: False
print(detect_cycle_sets_6(graph_with_self_loop))  # Expected output: True
print(detect_cycle_sets_6(empty_graph))  # Expected output: False
print(detect_cycle_sets_6(graph_disconnected))  # Expected output: True
print(detect_cycle_sets_6(large_graph_with_cycle))  # Expected output: True
