class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [(-a,'a'), (-b, 'b'), (-c, 'c')]
        max_heap = list(filter(lambda x: x[0] != 0, max_heap))
        heapq.heapify(max_heap)

        # # First Attempt:
        # def addToOutput(count, char, output):
        #     if count <= -2:
        #         if (not output) or (output and output[-1] != char):
        #             output.append(char)
        #             output.append(char)
        #             count += 2
        #         else:
        #             output.append(char)
        #             count += 1
        #     else:
        #         output.append(char)
        #         count += 1
        #     return count, char, output
        
        # while max_heap:
        #     used_chars = []
        #     if len(max_heap) == 1:
        #         count, char = max_heap[0]
        #         count, char, output = addToOutput(count, char, output)
        #         break

        #     count1, char1 = heapq.heappop(max_heap)
        #     count1, char1, output = addToOutput(count1, char1, output)
        #     count2, char2 = heapq.heappop(max_heap)
        #     output.append(char2)
        #     count2 += 1
        #     if count1 < 0:
        #         heapq.heappush(max_heap, (count1, char1))
            
        #     if count2 < 0:
        #         heapq.heappush(max_heap, (count2, char2))
            
        
        # return ''.join(output)


        # Simplified solution
        def addToOutput(count, char, output):
            output.append(char)
            count += 1
            return count, char, output

        if not max_heap:
            return ""
        
        first_count, first_char = heapq.heappop(max_heap)
        output = [first_char]
        first_count += 1
        if first_count < 0:
            heapq.heappush(max_heap, (first_count, first_char))

        while max_heap:
            count1, char1 = heapq.heappop(max_heap)
            if len(output) > 1 and output[-1] == char1 and output[-2] == char1:
                if max_heap:
                    count2, char2 = heapq.heappop(max_heap)
                    output.append(char2)
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(max_heap, (count2, char2))
                else:
                    break
            else:
                output.append(char1)
                count1 += 1
            if count1:
                heapq.heappush(max_heap, (count1, char1))
            
        return ''.join(output)
                




                