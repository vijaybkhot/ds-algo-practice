class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
            
        is_prime = [True] * (n)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n, p):
                    is_prime[i] = False
            p += 1

        primes = [i for i, prime in enumerate(is_prime) if prime]
        return len(primes)
            