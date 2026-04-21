class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        ans = ""
        for i in range(len(s)):
            i, j = self.check_palindrome(i, i, s)
            res = s[i:j+1]
            if len(res)>len(ans):
                ans = res
            i, j = self.check_palindrome(i, i+1, s)
            res = s[i:j+1]
            if len(res)>len(ans):
                ans = res
        return ans


    def check_palindrome(self, start, end, st):
        while start >=0 and end < len(st) and st[start] == st[end]:
            start-=1
            end+=1
        return start+1, end-1
            


        