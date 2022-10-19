# ввод значения N (эту переменную не менять)
N = int(input())

# здесь продолжайте программу
def get_sum(n):
    for i in range(1,n+2):
        yield sum(range(i))
for i in get_sum(N):
    print(i)