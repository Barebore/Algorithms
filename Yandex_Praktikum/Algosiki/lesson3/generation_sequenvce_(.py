def generate_all_parentheses(n):
    res = []
    def generate_helper(curr, left, right):
        if left == 0 and right == 0:
            res.append(curr)
        if left > 0:
            generate_helper(curr + "(", left - 1, right)
        if right > left:
            generate_helper(curr + ")", left, right - 1)
    generate_helper("", n, n)
    return res

n = int(input())
parentheses = generate_all_parentheses(n)
print(*parentheses, sep="\n")