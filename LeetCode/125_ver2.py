class Solution(object):
    def isPalindrome(self, s):
        result = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                result += char
        s = result
        print(s)
        s = s.replace(',', '').replace('.', '').replace(':', '').lower().replace(' ', '')
        return True if s == s[::-1] else False


a = 'aba'
b = Solution()
print(b.isPalindrome(a))