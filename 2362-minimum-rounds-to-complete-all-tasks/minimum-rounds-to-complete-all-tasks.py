class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        counter = Counter(tasks)
        if 1 in counter.values():
            return -1
        
        min_round = 0
        for level, freq in counter.items():
            if freq % 3 == 0:
                min_round += freq // 3
            elif freq % 3 == 1:
                freq -= 4
                min_round += 2
                min_round += freq // 3
            else:
                min_round += freq // 3
                min_round += 1
        
        return min_round

            
        