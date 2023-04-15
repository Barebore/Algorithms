class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        zipped_set = set(zip(s, t))
        print(list(zip(s,t)))
        print(zipped_set)
        return len(zipped_set) == len(set(s)) == len(set(t))
    

a = Solution()
print(a.isIsomorphic('egg', 'add'))