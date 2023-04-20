from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ''
    temp = strs[0]
    for word in strs:
        if temp == word[:len(temp)]:
            continue
        else:
            for j, letter in enumerate(temp):
                if letter == word[j]:
                    continue
                else:
                    temp = temp[:j]
                    break
            temp = word
    return temp

print(longestCommonPrefix(['ab', 'a']))
# print(longestCommonPrefix(["flower","flow","flight"]))