from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            print(result, '^', i, end = ' = ')
            result ^= i
            print(result)
        return result

a = Solution()
print(a.singleNumber([1,2,3,3,5,2,1]))