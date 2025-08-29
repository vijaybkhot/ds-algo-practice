class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # 4, 4
        # 4, 4
        # 1,2/ 2,1/ 2,3/ 3,2/ 3,4/ 4,3/ 
        n_odd = math.ceil(n/2)
        n_even = n//2
        m_odd = math.ceil(m/2)
        m_even = m//2

        return (n_odd*m_even + n_even*m_odd)
