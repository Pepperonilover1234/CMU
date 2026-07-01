name1 = input().strip()
name2 = input().strip()
name3 = input().strip()
names = [name1,name2,name3]
longest = max(names, key=len)
shortest = min(names, key=len)
print(longest, len(longest))
print(shortest, len(shortest))
