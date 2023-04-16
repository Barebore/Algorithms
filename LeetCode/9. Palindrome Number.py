class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


a = Solution()
print(a.isPalindrome(-121))