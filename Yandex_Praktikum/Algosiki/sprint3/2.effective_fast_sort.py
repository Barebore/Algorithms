# 87299335
def quicksort(arr, low, high):
    """
    Реализует алгоритм быстрой сортировки.
    
    Параметры:
    arr (list): список, который нужно отсортировать
    low (int): индекс начала сортировки
    high (int): индекс окончания сортировки
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """
    Выполняет разделение списка на подсписки в алгоритме быстрой сортировки.
    
    Параметры:
    arr (list): список, который нужно разделить
    low (int): индекс начала разделения
    high (int): индекс окончания разделения
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if compare(arr[j], pivot):
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def compare(a, b):
    """
    Сравнивает два кортежа по определенным правилам.
    
    Параметры:
    a (tuple): первый кортеж для сравнения
    b (tuple): второй кортеж для сравнения
    """
    return (a[1]*-1, a[2], a[0]) < (b[1]*-1, b[2], b[0])

def swap(arr, i, j):
    """
    Меняет местами два элемента списка.
    
    Параметры:
    arr (list): список, в котором нужно поменять элементы местами
    i (int): индекс первого элемента
    j (int): индекс второго элемента
    """
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    n = int(input())
    participants = []

    for _ in range(n):
        login, solved, penalty = input().split()
        participants.append((login, int(solved), int(penalty)))

    quicksort(participants, 0, n - 1)

    for participant in participants:
        print(participant[0])
