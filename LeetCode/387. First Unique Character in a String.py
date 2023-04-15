class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1 = s[:]
        for i in s:
            count = s.count(i)
            if count == 1:
                return s1.index(i)
            if s.count(i) > 1:
                s = s.replace(i, '')
        return -1
    
a = Solution()

print(a.firstUniqChar('abbcad'))