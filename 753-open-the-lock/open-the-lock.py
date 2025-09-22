class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        q.append(('0000', 0))
        visited = set(['0000'])
        deadends = set(deadends)

        if target in deadends or '0000' in deadends:
            return -1

        def getAdjacents(pos):
            adj = []
            pos_list = [int(num) for num in pos]
            for i in range(4):
                for move in (-1, 1):  # down, up
                    adj_pos = pos_list[:]
                    adj_pos[i] = (adj_pos[i] + move) % 10
                    adj.append(''.join(str(num) for num in adj_pos))
            return adj

        while q:
            curr_pos, level = q.popleft()
            if curr_pos == target:
                return level
            
            adj_pos = getAdjacents(curr_pos)
            for pos in adj_pos:
                if pos not in visited and pos not in deadends:
                    visited.add(pos)
                    q.append((pos, level+1))
        
        return -1
