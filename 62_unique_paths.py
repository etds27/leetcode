class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        We need to choose when the path moves downward within the m + n - 2 total moves
        The path goes downward m - 1 time

        The answer becomes m + n - 2 choose m - 1
        """
        #Total moves
        t = m + n - 2

        # Computing (m + n - 2)!
        m_n_2 = 1
        for i in range(1, t + 1):
            m_n_2 *= i

        # Computing (m - 1)!
        m_1 = 1
        for i in range(1, m):
            m_1 *= i

        # t - (m - 1) = m + n - 2 - m + 1 = n - 1
        # Computing (n - 1)!
        n_1 = 1
        for i in range(1, n):
            n_1 *= i

        # Choose formula
        # (m + n + 2)! / ((m - 1)! * (n - 1)!)
        ret = m_n_2 / (m_1 * n_1)
        return int(ret)
