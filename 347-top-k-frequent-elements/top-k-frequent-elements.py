class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def frequencyIndexMap(arr):
            map = {}
            for i in range(len(arr)):
                map[arr[i]] = map.get(arr[i],0)+1
            return map
        
        freqMap = frequencyIndexMap(nums)
        ferqMapTupleArray = tuple(freqMap.items())
        sortedTupleArray = sorted(ferqMapTupleArray, key=lambda x: x[1],  reverse=True)
        return map(lambda x:x[0], sortedTupleArray[0:k])
        