def find_index(search_element, arr):

    def index_translation(classic_index, length_arr, shift):
        if classic_index + shift >= length_arr:
            return classic_index - length_arr + shift
        else:
            return classic_index + shift

    def find_shift(arr):
        for i,value in enumerate(arr):
            if value > input_number[i+1]:
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

    length_arr = len(arr)
    shift = find_shift(arr)

    return binary_search(arr, search_element, length_arr, shift) + shift
    # result = []
    # # for i in range(length_arr):
    # #     result.append(input_number[index_translation(i, length_arr, shift)])


    # return input_number[index_translation(1,length_arr, shift)]


length_arr = int(input())
search_element = int(input())
input_number = list(map(int, input().split()))

# length_arr = 10
# search_element = 3
# input_number = [6,7,8,9,0,1,2,3,4,5]


# length_arr = 2
# search_element = 3
# input_number = [5,1]


# length_arr = 7
# search_element = 3
# input_number = [7,1,2,3,4,5,6]

print(find_index(search_element, input_number))
