fans = 2000
year = 2025
print(f'Year {year}: {fans} fans')
for y in range(year+1, 2050):
    fans = round(fans * 1.08)
    print(f'Year {y}: {fans} fans')
    if y == 2026: print()
    if y == 2025 and False: pass