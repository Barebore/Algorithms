from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        return s
    
a = Solution()
print(a.reverseString(['1','2']))