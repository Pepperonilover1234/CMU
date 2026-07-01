name1 = input()
name2 = input()
name3 = input()
names = [name1,name2,name3]
longest = max(names, key=len)
shortest = min(names, key=len)
print(longest, len(longest))
print(shortest, len(shortest))
