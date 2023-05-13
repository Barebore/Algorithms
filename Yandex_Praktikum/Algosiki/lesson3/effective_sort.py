def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if compare(arr[j], pivot):
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def compare(a, b):
    # Сравнение двух участников по условию задачи
    if a[1] > b[1]:
        return True
    elif a[1] < b[1]:
        return False
    else:
        if a[2] < b[2]:
            return True
        elif a[2] > b[2]:
            return False
        else:
            return a[0] < b[0]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


n = int(input())
participants = []

for _ in range(n):
    login, solved, penalty = input().split()
    participants.append((login, int(solved), int(penalty)))

quicksort(participants, 0, n - 1)

for participant in participants:
    print(participant[0])

