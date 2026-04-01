class Solution:
    def maxArea(self, nums: List[int]) -> int:
        water = 0
        l = 0
        r = len(nums)-1
        while l<r:
            current_water = min(nums[l], nums[r])*(r-l)
            water = max(water, current_water)
            if nums[l] <= nums[r]:
                l+=1
            else:
                r-=1
        return water

        