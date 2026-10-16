a = [1, 2, 3, 4, 5]
id_a = id(a)
print(id_a)
b = a.copy()
id_b = id(b)
print(id_b)
if id_a == id(b):
    result = "A"
elif id_a == id(a):
    result = "B"
elif id_b == id(b):
    result = "C"
else:
    result = "D"
print(result)
