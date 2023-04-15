class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = s[:]
        t1 = t[:]
        for i, word in enumerate(s):
            t = t.replace(t[i], word)

        for i, word in enumerate(t1):
            s1 = s1.replace(s1[i], word)
        print(s1,t1,s,t)
        return s1 == t1 and s == t

a = Solution()
print(a.isIsomorphic('paper', 'title'))