class Solution:
    def countSubstrings(self, s: str) -> int:
        c=0

        for i in range(len(s)):
            c+= self.check_palindrome(i, i, s)
            c+= self.check_palindrome(i, i+1, s)
        return c

    def check_palindrome(self, start, end, st):
        counter = 0
        while start >=0 and end < len(st) and st[start] == st[end]:
            counter+=1
            start-=1
            end+=1
        return counter
        