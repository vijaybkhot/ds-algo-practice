class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for prev, nxt in relations:
            graph[prev].add(nxt)
            indegree[nxt] += 1
        
        finish_time = [0]*(n+1)
        q = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                q.append(i)
                finish_time[i] = time[i - 1]
        
        while q:
            node = q.popleft()
        
            for nei in graph[node]:
                indegree[nei] -= 1
                finish_time[nei] = max(finish_time[nei], finish_time[node] + time[nei - 1])
                if indegree[nei] == 0:
                    q.append(nei)
                    

        return max(finish_time)
