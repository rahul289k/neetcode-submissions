class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            "}": "{", ")": "(", "]": "["
        }
        n = len(s)
        for i in range(n):
            if s[i] in mapper:
                if not stack or stack[-1] != mapper[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        return not stack

        