class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        freq_map = defaultdict(int)
        max_freq = 0
        for num in nums:
            freq_map[num]+= 1
            max_freq = max(max_freq, freq_map[num])
        
        # bucket = [[]*(max_freq+1)]
        # for num in nums:
        #     bucket[freq_map[num]].append(num)
        # res = []

        # for i in range(len(bucket)-1, -1, -1):
        #     while len(res) < k and bucket[i]:
        #         res.append(bucket[i].pop())
            
        # return res

        # Using a heap
        heap = [(-freq_map[num], num) for num in freq_map]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        
        return res
