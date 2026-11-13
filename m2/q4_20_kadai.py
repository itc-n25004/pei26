list_a = range(5, 26)
list_b = []
for i in list_a:
    if not (i % 2 == 0):
        list_b.append(i)

print(sum(list_b))
