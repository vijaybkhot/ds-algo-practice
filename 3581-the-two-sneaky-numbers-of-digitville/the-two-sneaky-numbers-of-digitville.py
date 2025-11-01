class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_set = set([num for num in range(len(nums)-2)])
        res = []
        for num in nums:
            if num not in num_set:
                res.append(num)
            else:
                num_set.remove(num)

        return res