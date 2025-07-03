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

        # # Solution using heap
        # def addCharToRes(s, char, count, heap):
        #     s += char
        #     count += 1
        #     if count < 0:
        #         heapq.heappush(heap, (count, char))
        #     return s

        # freq_count = Counter(s)
        # max_heap = [(-count, char) for char, count in freq_count.items()]
        # heapq.heapify(max_heap)
        
        # res = ""
        # prev_char = ""

        # while max_heap:
        #     count1, char1 = heapq.heappop(max_heap)
        #     if res and prev_char == char1:
        #         if max_heap:
        #             count2, char2 = heapq.heappop(max_heap)
        #             res = addCharToRes(res, char2, count2, max_heap)
        #         else:
        #             return ""
        #     res = addCharToRes(res, char1, count1, max_heap)
        #     prev_char = char1
        
        # return res


        # freq_count = defaultdict(int)
        # for char in s:
        #     freq_count[char] += 1
        
        # heap = [(-val, key) for key, val in freq_count.items()]
        # heapq.heapify(heap)

        # res = ""

        # while len(heap) > 1:
        #     count1, char1 = heapq.heappop(heap)
        #     count2, char2 = heapq.heappop(heap)
        #     res += char1 + char2
        #     count1 += 1
        #     count2 += 1
        #     if count1 < 0:
        #         heapq.heappush(heap, (count1, char1))
        #     if count2 < 0:
        #         heapq.heappush(heap, (count2, char2))
        
        # if heap:
        #     if heap[0][0] < -1 or (res and res[-1] == heap[0][1]):
        #         return ""
        #     else:
        #         res += heap[0][1]
        
        # return res
        
        freq = Counter(s)
        max_heap = [(-freq, char) for char, freq in freq.items()]
        heapq.heapify(max_heap)

        res = ""
        prev_char = ""

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            if res and prev_char == char1:
                if max_heap:
                    count2, char2 = heapq.heappop(max_heap)
                    res += char2
                    if count2 < -1:
                        heapq.heappush(max_heap, (count2+1, char2))
                else:
                    return ""
            res += char1
            prev_char = char1
            if count1 < -1:
                heapq.heappush(max_heap, (count1+1, char1))
        
        return res

            
            










