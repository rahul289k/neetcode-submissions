class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_val = set()
        for num in nums:
            if num in set_val:
                return True
            set_val.add(num)
        return False