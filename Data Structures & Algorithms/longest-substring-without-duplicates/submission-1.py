class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_data = set()
        n = len(s)
        l = 0
        ans = 0
        for r in range(n):
            while s[r] in set_data:
                set_data.remove(s[l])
                l+=1
            set_data.add(s[r])
            ans = max(r-l+1, ans)
        return ans

        