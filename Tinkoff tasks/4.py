import math

def task4(n):
    if n <= 2:
        return 0 

    def side_lenght(angles):
        if angles == 2:
            return 1
        sum_angles = (angles - 1) * 180
        cetner_alfa = sum_angles - ((angles - 1) * alfa)
        return 2 * r * math.sin(cetner_alfa * math.pi / 2 / 180)
        
    answer = 0

    if n == n_input:
        part_1 = n // 3 + 1
        part_2 = (n - part_1) // 2 + 2
        part_3 = n - part_1 - part_2 + 3
    else:
        part_1 = n
        part_2 = part_1 // 2 + 1
        part_3 = part_1 - part_2 + 1
        
    a = side_lenght(part_1)
    b = side_lenght(part_2)
    c = side_lenght(part_3)
    square_triangle = a * b * c / 4 / r
    answer += task4(part_1 - 2)
    answer += task4(part_2 - 2)
    answer += task4(part_3 - 2)
    answer += square_triangle
    return answer
n_input = int(input())
alfa = (n_input - 2) / n_input * 180
r = 1 / (2 * math.sin(math.pi / n_input))
print(task4(n_input))
