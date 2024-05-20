x, y, w, h = map(int, input().split())
way1 = w - x
way2 = h - y
print(min(x, y, way1, way2))