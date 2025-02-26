class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # # Sorting approach O(nlogn)
        # def frequencyIndexMap(arr):
        #     map = {}
        #     for i in range(len(arr)):
        #         map[arr[i]] = map.get(arr[i],0)+1
        #     return map
        
        # freqMap = frequencyIndexMap(nums)
        # ferqMapTupleArray = tuple(freqMap.items())
        # sortedTupleArray = sorted(ferqMapTupleArray, key=lambda x: x[1],  reverse=True)
        # return map(lambda x:x[0], sortedTupleArray[0:k])

        # Bucket sort approach O(n)
        def frequencyIndexMap(arr):
            map = {}
            for i in range(len(arr)):
                map[arr[i]] = map.get(arr[i],0)+1
            return map
        freqMap = frequencyIndexMap(nums)

        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in freqMap.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
        

        
        