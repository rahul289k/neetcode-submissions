class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n  = len(nums)+1
        res = 0
        for i in range(1, n):
            res = res^i
        for num in nums:
            res ^= num
        return res

        