# Generate a list to mark primes up to 10^6
MAX = 10**6 + 1
is_prime = [True] * MAX

def fill_primes():
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(MAX**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX, i):
                is_prime[j] = False

fill_primes()

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # def prime_divisors(n):
        #     primes = set()
        #     i = 2
        #     while i * i <= n:
        #         if n % i == 0:
        #             primes.add(i)
        #             while n % i == 0:
        #                 n //= i
        #         i += 1
        #     if n > 1:
        #         primes.add(n)
        #     return primes
        
        # def is_prime(n):
        #     if n <= 1:
        #         return False
        #     if n <= 3:
        #         return True  # 2 and 3 are primes
        #     if n % 2 == 0 or n % 3 == 0:
        #         return False

        #     # Only check up to sqrt(n), skipping even numbers
        #     for i in range(5, int(math.sqrt(n)) + 1, 6):
        #         if n % i == 0 or n % (i + 2) == 0:
        #             return False
        #     return True
        
        # n = len(nums)
        # min_jumps = [0]*n
        # prime_to_index = dict()
        # for i in range(n-1, -1, -1):
        #     if i == n-1:
        #         min_jumps[i] = 0
        #     else:
        #         min_jumps[i] = (1+min_jumps[i+1])
        #         if is_prime(nums[i]) and nums[i] in prime_to_index:
        #             min_jumps[i] = min(min_jumps[i], 1+min_jumps[prime_to_index[nums[i]]])
        #     primes = prime_divisors(nums[i])
        #     for prime in primes:
        #         if prime not in prime_to_index or min_jumps[prime_to_index[prime]] > min_jumps[i]:
        #             prime_to_index[prime] = i

        
        # return min_jumps[0]

        n = len(nums)
        maxi = max(nums)
        value_indices = defaultdict(list)
        
        for i, num in enumerate(nums):
            value_indices[num].append(i)

        dist = [-1] * n
        dist[0] = 0
        queue = deque([0])
        used = set()

        while queue:
            node = queue.popleft()

            # Move to adjacent positions
            for next_node in [node - 1, node + 1]:
                if 0 <= next_node < n and dist[next_node] == -1:
                    queue.append(next_node)
                    dist[next_node] = dist[node] + 1

            # If the current number is not prime or already processed, skip
            if not is_prime[nums[node]] or nums[node] in used:
                continue

            # Jump to all indices whose value is a multiple of current value
            for target in range(nums[node], maxi + 1, nums[node]):
                if target in value_indices:
                    for idx in value_indices[target]:
                        if dist[idx] == -1:
                            dist[idx] = dist[node] + 1
                            if idx == n - 1:
                                return dist[idx]
                            queue.append(idx)

            used.add(nums[node])

        return dist[-1]