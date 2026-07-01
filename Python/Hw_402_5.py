x = input()
z, y = map(int, input().split())

if x == '+':
    a = z + y
elif x == '-':
    a = z - y
elif x == '*':
    a = z * y
elif x == '/':
    a = z // y
else:
    print('Error')
    exit()

print(a)