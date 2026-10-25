a = 0b10111
b = 0b11101
c = a | b
print(c)


a = 6
b = pow(a, 3)
c = divmod(b, a)
print(c)


num = 3
list_a = []
while num < 5:
    for i in range(num, 10, 3):
        i -= 6
        list_a.append(i)
    num += 1
print(sum(list_a))


list_a = [4, 8, 3, 7, 9]
list_b = [10, 3, 6, 7, 2]
list_c = []
i = 0
while i < 5:
    if list_a[i] > list_b[i]:
        list_c.append(list_a[i] - list_b[i] ** 2)
    elif list_a[i] == list_b[i]:
        list_c.append(list_a[i] * 2 % 4)
    else:
        list_c.append(list_b[i] - list_a[i] // 2)
    i += 1
print(max(list_c))


list_a = ['Yokohama', 'Osaka', 'Nagoya', 'Sapporo', 'Fukuoka']
list_b = []
list_c = []
list_d = []
for name in list_a:
    if len(name) > 6:
        list_b.append(name)
    elif name.count('a') > 1:
        list_c.append(name)
    else:
        list_d.append(name)
print(list_c)


a = (27, 72)

if a[0] < 50 and a[1] < 50:
    print("補修")
elif a[0] >= 50 and a[1] >= 50:
    print("課題")
else:
    print("合格")


def func(a, b):
    if a**b <= 64:
        return 1
    else:
        return 0


x = func(4, 3)
y = func(3, 4)
z = [bool(x), bool(y)]
print(z)
