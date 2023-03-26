n = int(input()) # количество точек
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

max_area = 0
for i in range(n-1):
    for j in range(i+1, n):
        dx = abs(points[i][0] - points[j][0])
        dy = abs(points[i][1] - points[j][1])
        if dx > 0 and dy > 0:
            area = dx * dy
            if area > max_area:
                max_area = area

print(max_area)
