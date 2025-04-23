class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_map = {}
        largest_size = 0
        largest_count = 0
        for i in range(1, n+1):
            sum_digits = 0
            while i > 0:
                sum_digits += i % 10
                i = i // 10
            if sum_digits not in sum_map:
                sum_map[sum_digits] = []

            sum_map[sum_digits].append(i)

            if len(sum_map[sum_digits]) > largest_size:
                largest_size = len(sum_map[sum_digits])
                largest_count = 0
            if len(sum_map[sum_digits]) == largest_size:
                largest_count += 1

        return largest_count
        