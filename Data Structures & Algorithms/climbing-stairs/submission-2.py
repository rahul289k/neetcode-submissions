class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        sec_prev = 1
        first_prev = 2
        ans = 0
        for i in range(3, n+1):
            ans = sec_prev + first_prev
            sec_prev = first_prev
            first_prev = ans
        return ans
        