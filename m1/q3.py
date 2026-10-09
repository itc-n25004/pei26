a = 12
b = 5
print(b-a)
print(b-abs(2*b-a)*3)
print("{0:05b}".format(b))

c = [2,7,15,19]
c.sort()

print([bin(x) for x in c])


print(f'{a-b/c[3]:8.3f}')

``` format 指定の仕方
-: 左詰め
+: 右詰め
: 中央詰め
>:右揃え
8:8桁
3:小数点以下3桁
f:float型