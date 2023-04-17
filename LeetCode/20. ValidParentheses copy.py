class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        dct = {
            ']':'[',
            '}': '{',
            ')': '('
        }
        for bracket in s:
            if bracket in ['(', '{', '[']:
                result.append(bracket)
            elif bracket in [']',')', '}'] and result[-1] == dct[bracket]:
                result.pop()
            else:
                return False
        return True
        
a = Solution()
print(a.isValid('(('))
print()