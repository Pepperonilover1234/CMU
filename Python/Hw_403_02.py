N = input()
count_G = 0
count_P = 0
count_F = 0
for i in range(N):
    x = int(input())
    if x >= 80:
        count_G += 1
    elif x >= 50:
        count_P += 1
    else:
        count_F += 1
print(count_G, count_P, count_F)
