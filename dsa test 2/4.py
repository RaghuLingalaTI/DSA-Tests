a = input().split(", ")
list_a = []
for i in a:
    if i not in list_a:
        list_a.append(i)
print(*list_a)