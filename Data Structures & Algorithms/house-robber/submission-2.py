class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        sec_prev = nums[0]
        first_prev = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            curr = max(sec_prev+nums[i], first_prev)
            sec_prev = first_prev
            first_prev = curr
        return first_prev

        