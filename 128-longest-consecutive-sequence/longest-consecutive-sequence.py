class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_len = 1
                curr_num = num
                while curr_num+1 in nums_set:
                    curr_len += 1
                    curr_num += 1
                res = max(res, curr_len)
        
        return res



















        # res = 0
        # nums_set = set(nums)


        # for num in nums_set:
        #     if num-1 not in nums_set:
        #         current = num
        #         streak = 1

        #         while current+1 in nums_set:
        #             streak += 1
        #             current+= 1
        #         res = max(streak, res)
        
        # return res