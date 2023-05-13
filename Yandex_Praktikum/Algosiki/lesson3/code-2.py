def broken_search(nums, target) -> int:
    def index_translation(classic_index, length_arr, shift):
        if classic_index + shift >= length_arr:
            return classic_index - length_arr + shift
        else:
            return classic_index + shift

    def find_shift(arr, length_arr):
        for i,value in enumerate(arr):
            if i + 1 >= length_arr:
                return 0
            if value > arr[i+1]:
                return i + 1
    
    def binary_search(arr, target, length_arr, shift):
        left, right = 0, length_arr - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[index_translation(mid, length_arr, shift)] == target:
                return mid
            elif arr[index_translation(mid, length_arr, shift)] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    length_arr = len(nums)
    if length_arr == 1:
        return 0 if target == nums[0] else -1
    shift = find_shift(nums, length_arr)
    result = binary_search(nums, target, length_arr, shift)

    return result + shift if result != -1 else result

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


# length_arr = int(input())
# search_element = int(input())
# input_number = list(map(int, input().split()))


# print(broken_search(input_number, search_element))