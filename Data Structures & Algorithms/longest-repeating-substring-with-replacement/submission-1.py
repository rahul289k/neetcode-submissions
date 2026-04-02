class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map_data = {}
        max_freq = 0
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            map_data[s[r]] = map_data.get(s[r], 0)+1
            max_freq = max(max_freq, map_data[s[r]])
            while (r-l+1 - max_freq) > k:
                map_data[s[l]] = map_data[s[l]] - 1
                if map_data[s[l]] == 0:
                    del map_data[s[l]]
                l+=1
            ans = max(ans, r-l+1)
        return ans
            





        
        