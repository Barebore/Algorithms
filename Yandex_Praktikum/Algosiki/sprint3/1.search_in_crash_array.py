# 87298172
def find_shift(arr):
    '''
    Функция для поиска смещения в отсортированном и сдвинутом массиве.
    
    Параметры:
    arr (list): Входной массив.
    
    Возвращает:
    int: Индекс точки смещения.
    '''
    low, high = 0, len(arr) - 1
    if arr[low] < arr[high]:
        return 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        else:
            if arr[mid] < arr[low]:
                high = mid - 1
            else:
                low = mid + 1

def binary_search(arr, target, start, end):
    '''
    Функция для выполнения бинарного поиска в массиве.
    
    Параметры:
    arr (list): Входной массив.
    target (int): Искомое значение.
    start (int): Индекс начала поиска.
    end (int): Индекс окончания поиска.
    
    Возвращает:
    int: Индекс искомого элемента или -1, если элемент не найден.
    '''
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def broken_search(nums, target):
    '''
    Функция для поиска элемента в отсортированном и сдвинутом массиве.
    
    Параметры:
    nums (list): Входной массив.
    target (int): Искомое значение.
    
    Возвращает:
    int: Индекс искомого элемента или -1, если элемент не найден.
    '''
    length_arr = len(nums)
    if length_arr == 1:
        return 0 if target == nums[0] else -1

    shift = find_shift(nums)
    if nums[shift] == target:
        return shift
    if shift == 0:
        return binary_search(nums, target, 0, length_arr - 1)

    if target < nums[0]:
        return binary_search(nums, target, shift, length_arr - 1)
    return binary_search(nums, target, 0, shift)

if __name__ == "__main__":
    pass
