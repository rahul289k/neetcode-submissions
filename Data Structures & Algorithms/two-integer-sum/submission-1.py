class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_data = {}
        for i in range(len(nums)):
            sec_elem = target -  nums[i]
            if sec_elem in map_data:
                return [map_data[sec_elem], i]
            else:
                map_data[nums[i]] = i
                

        