letters = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

def generate_combinations(digits, curr='', i=0):
    if i == len(digits):
        print(curr, end = ' ')
        return
    for letter in letters[int(digits[i])]:
        generate_combinations(digits, curr + letter, i + 1)

digits = input()
generate_combinations(digits)
