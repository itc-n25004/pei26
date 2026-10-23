# 偶数の2乗を格納するlistを作成
a_list = []
for i in range(1, 9):
    # 変数bにiの2乗を代入
    b = i**2
    # listにbを追加
    a_list.append(b)
print(a_list)