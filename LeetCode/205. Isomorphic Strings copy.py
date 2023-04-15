class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct_s = dict()
        dct_t = dict()
        for i in range(len(s)):
            if s[i] in dct_s:
                dct_s[s[i]] += 1
            else:
                dct_s[s[i]] = 0                
            if t[i] in dct_t:
                dct_t[t[i]] += 1
            else:
                dct_t[t[i]] = 0

            # print(dct_s.values())
            # print(dct_t.values())
            # print(list(dct_s.values()))
            # print(list(dct_t.values()))
            if list(dct_s.values()) != list(dct_t.values()):
                return False
        return True



a = Solution()
print(a.isIsomorphic('foo', 'bar'))