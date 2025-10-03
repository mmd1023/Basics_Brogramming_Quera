a, b = map(int, input().split())

h = 0 if a == 0 else 12-a
m = 0 if b == 0 else 60-b

print(f'{h:02d}:{m:02d}')