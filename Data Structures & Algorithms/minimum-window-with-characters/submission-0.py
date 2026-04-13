class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0)+1
        need = len(t_freq)
        have = 0
        s_freq = {}
        flag = float('inf')
        res = ""
        
        l = 0
        for r in range(len(s)):
            s_freq[s[r]] = s_freq.get(s[r], 0)+1
            if s[r] in t_freq and s_freq[s[r]] == t_freq[s[r]]:
                have+=1
            while have == need:
                if flag > (r-l+1):
                    res = s[l:r+1]
                    flag = r-l+1
                s_freq[s[l]] -=1
                if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                    if s_freq[s[l]] == 0:
                        del s_freq[s[l]]
                    have-=1
                l+=1

        return res if flag != float('inf') else ""
                
                




            






        