def twoSum(nums, target):
    previous = set()

    for A in nums:
        Y = target - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    return None, None

print(twoSum(list(map(int, input().split())),int(input())))