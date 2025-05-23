class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # # Attempt 1: One directional BFS: 
        # def get_neighbors(pos):
        #     pos_arr = [num for num in pos]
        #     adjacent = []
        #     for i in range(len(pos)):
        #         curr_num = int(pos_arr[i])
        #         next_num = 0 if curr_num == 9 else curr_num+1
        #         prev_num = 9 if curr_num == 0 else curr_num - 1
        #         pos_arr[i] = str(next_num)
        #         adjacent.append(''.join(pos_arr))
        #         pos_arr[i] = str(prev_num)
        #         adjacent.append(''.join(pos_arr))
        #         pos_arr[i] = str(curr_num)
        #     return adjacent

        # deadends_set = set(deadends)

        # if "0000" in deadends_set:
        #     return -1

        # q = deque()
        # visited = set()
        # q.append("0000")
        # visited.add("0000")
        # dist = 0
        # while q:
        #     for _ in range(len(q)):
        #         curr_node = q.popleft()
        #         if curr_node == target:
        #             return dist
        #         neighbors = get_neighbors(curr_node)
        #         for neighbor in neighbors:
        #             if neighbor in deadends_set or neighbor in visited:
        #                 continue
        #             visited.add(neighbor)
        #             q.append(neighbor)
        #     dist += 1
        
        # return -1

        # Bidirectional BFS
        def get_neighbors(pos):
            adjacent = []
            for i in range(4):
                digit = int(pos[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    neighbor = pos[:i] + str(new_digit) + pos[i+1:]
                    adjacent.append(neighbor)
            return adjacent

        dead = set(deadends)
        if "0000" in dead or target in dead:
            return -1
        if target == "0000":
            return 0

        # Initialize BFS from both ends
        visited = set()
        begin_set = {"0000"}
        end_set = {target}
        steps = 0

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            temp = set()
            for pos in begin_set:
                if pos in dead:
                    continue
                if pos in end_set:
                    return steps
                visited.add(pos)
                for neighbor in get_neighbors(pos):
                    if neighbor not in visited and neighbor not in dead:
                        temp.add(neighbor)
            begin_set = temp
            steps += 1
        
        return -1
