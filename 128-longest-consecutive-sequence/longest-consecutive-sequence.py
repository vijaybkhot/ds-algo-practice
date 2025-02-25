class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return 0
        # res = []
        # unique_nums = list(set(nums))
        # unique_nums.sort()
        # curr_sequence = 1
        # for i in range(0, len(unique_nums)-1):
        #     if unique_nums[i+1] == unique_nums[i] + 1:
        #         curr_sequence += 1
        #     else:
        #         res.append(curr_sequence)
        #         curr_sequence = 1
        # res.append(curr_sequence)
        # return max(res)

        if not nums:
            return 0
        longest_streak = 0
        unique_nums = set(nums)
        for num in unique_nums:
            if num-1 not in unique_nums:
                curr_streak = 1
                curr_num = num

                while curr_num + 1 in unique_nums:
                    curr_num += 1
                    curr_streak += 1
                
                if curr_streak > longest_streak:
                    longest_streak = curr_streak
                
        return longest_streak
