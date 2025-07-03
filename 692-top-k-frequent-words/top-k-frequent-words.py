class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1
        
        res = [(-freq, word) for word, freq in counter.items()]
        res.sort()
        return [word for _, word in res][:k]
        