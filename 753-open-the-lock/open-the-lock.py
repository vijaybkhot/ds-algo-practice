class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # num_graph = {
        #     '0': ['1', '9'],
        #     '1': ['2', '0'],
        #     '2': ['3', '1'],
        #     '3': ['4', '2'],
        #     '4': ['5', '3'],
        #     '5': ['6', '4'],
        #     '6': ['7', '5'],
        #     '7': ['8', '6'],
        #     '8': ['9', '7'],
        #     '9': ['0', '8']
        # }
        # deadends_set = set(deadends)
        # if '0000' in deadends_set or target in deadends_set:
        #     return -1
        # q = deque()
        # q.append('0000')
        # visited = set()
        # level = 0
        # while q:
        #     for _ in range(len(q)):
        #         curr_node = q.popleft()
        #         if curr_node == target:
        #             return level
        #         for idx, char in enumerate(curr_node):
        #             for nei in num_graph[char]:
        #                 new_node = curr_node[:idx] + nei + curr_node[idx+1:]
        #                 if new_node == target:
        #                     return level+1
        #                 if new_node not in deadends and new_node not in visited:
        #                     visited.add(new_node)
        #                     q.append(new_node)
        #     level += 1
        
        # return -1

        #  Without using a graph
        def get_adjacents(pos):
            pos_array = [num for num in pos]
            adjacent = []
            for i in range(len(pos_array)):
                num = int(pos_array[i])
                for direction in [1, -1]:
                    new_num =( num + direction) % 10
                    pos_array[i] = str(new_num)
                    adjacent.append(''.join(pos_array))
                pos_array[i] = str(num)
            return adjacent
        
        deadends_set = set(deadends)


        if '0000' in deadends_set or target in deadends_set:
            return -1
        
        # Multi- source dfs
        left, right = deque(), deque()
        left.append('0000')
        right.append(target)
        left_level, right_level = 0, 0
        visited_left = set(['0000'])
        visited_right = set([target])

        while left and right:
            if len(right) < len(left):
                left, right = right, left
                left_level, right_level = right_level, left_level
                visited_left, visited_right = visited_right, visited_left

            for _ in range(len(left)):
                curr_node = left.popleft()
                if curr_node in visited_right:
                    return left_level+right_level
                adjacents = get_adjacents(curr_node)
                for new_node in adjacents:
                    if new_node in visited_right:
                        return left_level+right_level+1
                    elif new_node not in visited_left and new_node not in deadends_set:
                        visited_left.add(new_node)
                        left.append(new_node)
            left_level += 1
        
        return -1




        # #Single source BFS
        # q = deque()
        # q.append('0000')
        # visited = set()

        # level = 0
        # while q:
        #     for _ in range(len(q)):
        #         curr_node = q.popleft()
        #         if curr_node == target:
        #             return level
        #         adjacents = get_adjacents(curr_node)
        #         for new_node in adjacents:
        #             if new_node == target:
        #                 return level + 1
        #             if new_node not in visited and new_node not in deadends_set:
        #                 visited.add(new_node)
        #                 q.append(new_node)
        #     level += 1

        # return -1




        


        # # # Attempt 1: One directional BFS: 
        # # def get_neighbors(pos):
        # #     pos_arr = [num for num in pos]
        # #     adjacent = []
        # #     for i in range(len(pos)):
        # #         curr_num = int(pos_arr[i])
        # #         next_num = 0 if curr_num == 9 else curr_num+1
        # #         prev_num = 9 if curr_num == 0 else curr_num - 1
        # #         pos_arr[i] = str(next_num)
        # #         adjacent.append(''.join(pos_arr))
        # #         pos_arr[i] = str(prev_num)
        # #         adjacent.append(''.join(pos_arr))
        # #         pos_arr[i] = str(curr_num)
        # #     return adjacent

        # # deadends_set = set(deadends)

        # # if "0000" in deadends_set:
        # #     return -1

        # # q = deque()
        # # visited = set()
        # # q.append("0000")
        # # visited.add("0000")
        # # dist = 0
        # # while q:
        # #     for _ in range(len(q)):
        # #         curr_node = q.popleft()
        # #         if curr_node == target:
        # #             return dist
        # #         neighbors = get_neighbors(curr_node)
        # #         for neighbor in neighbors:
        # #             if neighbor in deadends_set or neighbor in visited:
        # #                 continue
        # #             visited.add(neighbor)
        # #             q.append(neighbor)
        # #     dist += 1
        
        # # return -1

        # # Bidirectional BFS
        # def get_neighbors(pos):
        #     adjacent = []
        #     for i in range(4):
        #         digit = int(pos[i])
        #         for move in [-1, 1]:
        #             new_digit = (digit + move) % 10
        #             neighbor = pos[:i] + str(new_digit) + pos[i+1:]
        #             adjacent.append(neighbor)
        #     return adjacent

        # dead = set(deadends)
        # if "0000" in dead or target in dead:
        #     return -1
        # if target == "0000":
        #     return 0

        # # Initialize BFS from both ends
        # visited = set()
        # begin_set = {"0000"}
        # end_set = {target}
        # steps = 0

        # while begin_set and end_set:
        #     if len(begin_set) > len(end_set):
        #         begin_set, end_set = end_set, begin_set
            
        #     temp = set()
        #     for pos in begin_set:
        #         if pos in dead:
        #             continue
        #         if pos in end_set:
        #             return steps
        #         visited.add(pos)
        #         for neighbor in get_neighbors(pos):
        #             if neighbor not in visited and neighbor not in dead:
        #                 temp.add(neighbor)
        #     begin_set = temp
        #     steps += 1
        
        # return -1
