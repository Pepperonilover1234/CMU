
amount = int(input())
denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
counts = []

for denom in denominations:
    count = amount // denom
    counts.append(count)
    amount = amount % denom

print(' '.join(map(str, counts)))