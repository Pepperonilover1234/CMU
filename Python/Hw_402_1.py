s = input()

if s == 's':
    x = int(input())
    area = x * x
else:
    x, y = map(int, input().split())
    area = x * y

print(area)