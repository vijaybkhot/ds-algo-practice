class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probs = [0]*n
        graph = defaultdict(set)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].add((v, prob))
            graph[v].add((u, prob))
        probs[start_node] = 1
        heap = []
        heapq.heappush(heap, (-1, start_node)) # arrival_prob, node

        while heap:
            curr_prob, node = heapq.heappop(heap)
            curr_prob = -1 * curr_prob
            if curr_prob < probs[node]:
                continue
            for nxt_node, nxt_prob in graph[node]:
                new_prob = curr_prob * nxt_prob
                if new_prob > probs[nxt_node]:
                    probs[nxt_node] = new_prob
                    heapq.heappush(heap, (-new_prob, nxt_node))
        
        res = probs[end_node]
        return res if res != 1 else 0
