class Solution(object):
    def isPalindrome(self, s):
        result = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                result += char
        s = result
        print(s)
        s = s.replace(',', '').replace('.', '').replace(':', '').lower().replace(' ', '')
        if len(s) % 2 == 1:
            first_part = s[:len(s)//2]
            second_part = s[:len(s)//2:-1]
        else:
            first_part = s[:len(s) // 2]
            second_part = s[:len(s) // 2 - 1:-1]
        return True if first_part == second_part else False


a = '0P'
b = Solution()
print(b.isPalindrome(a))