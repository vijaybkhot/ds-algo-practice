from sortedcontainers import SortedSet

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        component_map = defaultdict(SortedSet)
        node_component_map = defaultdict(int)
        curr_component = 1

        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        def dfs(node, curr_component):
            if node in visited:
                return
            visited.add(node)
            component_map[curr_component].add(node)
            node_component_map[node] = curr_component
            for nei in graph[node]:
                dfs(nei, curr_component)

            
        for node in range(1, c+1):
            if node not in visited:
                dfs(node, curr_component)
                curr_component += 1
        
        res = []

        for query_type, node in queries:
            # get the component for the node
            component = node_component_map[node]
            if query_type == 1:
                # check if the node is present in the component map
                if node in component_map[component]:
                    res.append(node)
                else:
                    if component_map[component]:
                        res.append(component_map[component][0])
                    else:
                        res.append(-1)
            else:
                if node in component_map[component]:
                    component_map[component].remove(node)
        
        return res
                


        
        