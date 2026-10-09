# 絶対値の表記
print(abs(-7))
#2進数を8桁で左埋め
print(f'{bin(64):>8}')
#  降順でソート
c = [2,7,15,12,9]
result = sorted(c, reverse=True)
print(result)
# スライスで表記
print(c[-2:],c[1])

#関数で8桁で小数点1桁の右余白-で左詰めをフォーマット
def format_float(num):
    return f'{num:-<8.1f}'