import itertools

n = int(input())


nails = []
for i in range(n):
    x, y = map(int, input().split())
    nails.append((x, y))

max_area = 0

for corners in itertools.combinations(nails, 4):
    x_values = [c[0] for c in corners]
    y_values = [c[1] for c in corners]
    if len(set(x_values)) == 2 and len(set(y_values)) == 2:
        x1 = min(x_values)
        y1 = min(y_values)
        x2 = max(x_values)
        y2 = max(y_values)
        area = (x2 - x1) * (y2 - y1)
        if area > max_area:
            max_area = area

print(max_area)
