class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            count = s.count(i)
            if count == 1:
                return i
            if s.count(i) > 1:
                s = s.replace(i, '')
        return -1
    
a = Solution()

print(a.firstUniqChar('abbcad'))