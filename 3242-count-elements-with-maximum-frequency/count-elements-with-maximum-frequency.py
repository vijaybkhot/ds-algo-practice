class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        res = 0

        for num, freq in count.items():
            if freq == max_freq:
                res += 1
        
        return res*max_freq