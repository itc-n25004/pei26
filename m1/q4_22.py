a = 17
b = 5
dm = divmod(a, b)
p = pow(dm[0], dm[1])

all_num = [ a, b, dm[0], dm[1], p]
min_all_num = min(all_num)
max_all_num = max(all_num)
sum_all = sum(all_num)

print(f"min: {min_all_num}, max: {max_all_num}, sum: {sum_all}")
