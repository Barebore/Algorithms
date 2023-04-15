from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = dict()
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 0
        return max(dct, key=dct.get)
    
a = Solution()
print(a.majorityElement([3,2,3]))
print(a.majorityElement([2,2,1,1,1,2,2]))