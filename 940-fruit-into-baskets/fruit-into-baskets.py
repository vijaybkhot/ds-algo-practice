class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0 # 4
        #           l
        # [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
        #              r
        left = 0
        curr_dict = dict()    # {1, 2}
        for right in range(len(fruits)):
            curr_dict[fruits[right]] = curr_dict.get(fruits[right], 0) + 1
            while left < right and len(curr_dict) > 2:
                curr_dict[fruits[left]] -= 1
                if curr_dict[fruits[left]] == 0:
                    del curr_dict[fruits[left]]
                left += 1
            res = max(res, right-left+1)
        return res
            
