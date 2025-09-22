class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # q = deque()
        # q.append(('0000', 0))
        # visited = set(['0000'])
        deadends = set(deadends)

        if target in deadends or '0000' in deadends:
            return -1
        
        if target == '0000':
            return 0

        def getAdjacents(pos):
            adj = []
            pos_list = [int(num) for num in pos]
            for i in range(4):
                for move in (-1, 1):  # down, up
                    adj_pos = pos_list[:]
                    adj_pos[i] = (adj_pos[i] + move) % 10
                    adj.append(''.join(str(num) for num in adj_pos))
            return adj

        # while q:
        #     curr_pos, level = q.popleft()
        #     if curr_pos == target:
        #         return level
            
        #     adj_pos = getAdjacents(curr_pos)
        #     for pos in adj_pos:
        #         if pos not in visited and pos not in deadends:
        #             visited.add(pos)
        #             # q.append((pos, level+1))
        #             q.append(pos)
        
        # return -1

        left, right = deque(['0000']), deque([target])
        left_level, right_level = 0, 0
        visited_left = set()
        visited_right = set()

        while left and right:
            if len(right) < len(left):
                left, right = right, left
                left_level, right_level = right_level, left_level
                visited_left, visited_right = visited_right, visited_left

            for _ in range(len(left)):
                curr_pos = left.popleft()
                if curr_pos in visited_right:
                    return left_level + right_level
                adj_pos = getAdjacents(curr_pos)
                for pos in adj_pos:
                    if pos not in visited_left and pos not in deadends:
                        visited_left.add(pos)
                        left.append(pos)
            left_level += 1
        
        return -1