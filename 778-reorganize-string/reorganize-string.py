class Solution:
    def reorganizeString(self, s: str) -> str:
        # freq_count = Counter(s)
        # output = ""
        # while freq_count:
        #     if len(freq_count) == 1 and list(freq_count.values())[0] > 1:
        #         return ""
        #     keys = [char for char in freq_count]
        #     for key in keys:
        #         output += key
        #         freq_count[key] -= 1
        #         if freq_count[key] == 0:
        #             del freq_count[key]
        
        # return output

        # Solution using heap
        freq_count = Counter(s)
        max_heap = [(-count, char) for char, count in freq_count.items()]
        heapq.heapify(max_heap)
        
        res = ""

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            if res and res[-1] == char1:
                if max_heap:
                    count2, char2 = heapq.heappop(max_heap)
                    res += char2
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(max_heap, (count2, char2))
                else:
                    return ""
            res += char1 
            count1 += 1
            if count1 < 0:
                heapq.heappush(max_heap, (count1, char1))
        
        return res