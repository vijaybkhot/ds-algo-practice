class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        i = 0
        for i in range(0, n, 3):
            start = nums[i]
            for j in range(1, 3):
                if nums[i+j] > start+k:
                    return []
        return [nums[i:i+3] for i in range(0, n, 3)]

        while i < len(nums):
            curr_arr = [nums[i]]
            start = nums[i]
            for j in range(1, 3):
                curr_num = nums[i+j]
                if curr_num > start+k:
                    return []
                curr_arr.append(curr_num)
            if len(curr_arr) != 3:
                return []
            res.append(curr_arr)
            i += 3
        return res

        