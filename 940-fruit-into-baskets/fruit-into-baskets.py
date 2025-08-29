class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        curr_fruit_map = Counter()
        left = 0
        res = 0
        
        for right in range(len(fruits)):
            curr_fruit_map[fruits[right]] += 1
            while left <= right and len(curr_fruit_map) > 2:
                curr_fruit_map[fruits[left]] -= 1
                if curr_fruit_map[fruits[left]] == 0:
                    del curr_fruit_map[fruits[left]]
                left += 1
            
            res = max(res, right-left+1)
        
        return res
