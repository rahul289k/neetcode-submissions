class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_data = {}

        sm = 0
        res = float('-inf')
        for i in range(len(nums)):
            sm+=nums[i]
            res = max(sm, res)
            if sm<0:
                sm = 0
        return res
            

            

        