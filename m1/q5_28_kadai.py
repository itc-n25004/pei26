#  default list
days = ["月", "月", "火", "水", "木", "金", "金"]

# remove method
days.remove("月")
days.remove("金")

# 最後に土日の追加(insert)
days.insert(6, "土")
days.insert(0, "日")

print(days)
